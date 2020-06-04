CBR
===========

Provides functionality to get official CBR (Central Bank of Russia) exchange rates. Typical usage
often looks like this:

    #!/usr/bin/env python

    from cbr import get_exchange_rates

    get_exchange_rates('15.05.2010')
    get_exchange_rates('13.01.2020', codes=['840', '978'])
    get_exchange_rates('13.01.2020', code='840')
    get_exchange_rates('13.01.2020', symbols=['USD', 'EUR'])
    get_exchange_rates('13.01.2020', symbol='JPY')

Result is array like this:

    [{'code': '392', 'symbol': 'JPY', 'amount': 100, 'rate': Decimal('55.9098')}]

(Note amount column, it's not always 1)

Raises an InvalidDateArgException if date < 01.07.1992 or > today.

Русский:
=========

Библиотека для получения официальных курсов ЦБ на дату (для использования в расчетах деклараций и пр.). 

Кидает исключение InvalidDateArgException если данных на дату нет.
