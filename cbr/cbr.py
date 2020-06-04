import urllib.request
from bs4 import BeautifulSoup
from decimal import Decimal


class InvalidDateArgException(Exception):
    pass


def get_exchange_rates(date, **kwargs):
    """
    :param date: date in format dd.mm.yyyy
    :param symbol: single symbol (optional)
    :param symbols: array of symbols (optional)
    :param code: array of codes (optional)
    :param codes: array of codes (optional)
    :return: returns array of exchange rates
    """
    _URL = 'http://cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To={}'  # nopep8

    res = []

    with urllib.request.urlopen(_URL.format(date)) as f:
        data = f.read().decode('utf-8')
    code = kwargs.get('code')
    codes = kwargs.get('codes')
    symbol = kwargs.get('symbol')
    symbols = kwargs.get('symbols')
    if symbols:
        symbols = [x.upper() for x in symbols]
    if symbol:
        symbol = symbol.upper()

    page = BeautifulSoup(data, features="html.parser")

    button = page.find('button', {'class': 'datepicker-filter_button'})
    if button is None or button.string != date:
        raise InvalidDateArgException

    table = page.find('table', {'class': 'data'})
    th = table.tbody.tr.find_all('th')
    assert len(th) == 5

    for tr in table.tbody.find_all('tr'):
        tds = tr.find_all('td')
        if len(tds):
            td_symbol = tds[1].string
            td_code = tds[0].string
            # apply filters:
            if symbols and td_symbol.upper() not in symbols:
                continue
            if symbol and td_symbol.upper() != symbol:
                continue
            if codes and td_code not in codes:
                continue
            if code and td_code != code:
                continue

            res.append({
                'code': td_code,
                'symbol': td_symbol,
                'amount': int(tds[2].string),
                'rate': Decimal(tds[4].string.replace(',', '.')),
            })
    return res
