import urllib.request
import xml.etree.ElementTree as ET
from decimal import Decimal


def get_exchange_rates(date, **kwargs):
    """
    :param date: date in format dd.mm.yyyy
    :param symbol: single symbol (optional)
    :param symbols: array of symbols (optional)
    :param code: array of codes (optional)
    :param codes: array of codes (optional)
    :return: returns array of exchange rates
    """
    _URL = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req={}'
    res = []

    with urllib.request.urlopen(_URL.format(date)) as f:
        data = f.read()  #.decode('utf-8')
    code = kwargs.get('code')
    codes = kwargs.get('codes')
    symbol = kwargs.get('symbol')
    symbols = kwargs.get('symbols')
    if symbols:
        symbols = [x.upper() for x in symbols]
    if symbol:
        symbol = symbol.upper()

    root = ET.fromstring(data)
    for valute in root.findall('Valute'):
        td_code = valute.find('NumCode').text
        td_symbol = valute.find('CharCode').text

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
            'amount': int(valute.find('Nominal').text),
            'rate': Decimal(valute.find('Value').text.replace(',', '.')),
        })
    return res
