from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import Decimal


SUPPORTED_CURRENCIES = [{'EUR': 'Euro Member Countries'},
                        {'IDR': 'Indonesia Rupiah'},
                        {'BGN': 'Bulgaria Lev'},
                        {'ILS': 'Israel Shekel'},
                        {'GBP': 'United Kingdom Pound'},
                        {'DKK': 'Denmark Krone'},
                        {'CAD': 'Canada Dollar'},
                        {'JPY': 'Japan Yen'},
                        {'HUF': 'Hungary Forint'},
                        {'RON': 'Romania New Leu'},
                        {'MYR': 'Malaysia Ringgit'},
                        {'SEK': 'Sweden Krona'},
                        {'SGD': 'Singapore Dollar'},
                        {'HKD': 'Hong Kong Dollar'},
                        {'AUD': 'Australia Dollar'},
                        {'CHF': 'Switzerland Franc'},
                        {'KRW': 'South Korea Won'},
                        {'CNY': 'China Yuan Renminbi'},
                        {'TRY': 'Turkey Lira'},
                        {'HRK': 'Croatia Kuna'},
                        {'NZD': 'New Zealand Dollar'},
                        {'THB': 'Thailand Baht'},
                        {'USD': 'United States Dollar'},
                        {'NOK': 'Norway Krone'},
                        {'RUB': 'Russia Ruble'},
                        {'INR': 'India Rupee'},
                        {'MXN': 'Mexico Peso'},
                        {'CZK': 'Czech Republic Koruna'},
                        {'BRL': 'Brazil Real'},
                        {'PLN': 'Poland Zloty'},
                        {'PHP': 'Philippines Peso'},
                        {'ZAR': 'South Africa Rand'}]

cr = CurrencyRates()
cc = CurrencyCodes()


def convert(request):
    # Get currencies
    from_curr = request['from-currency']
    to_curr = request['to-currency']

    # Get currency symbols
    in_symbol = cc.get_symbol(from_curr)
    converted_symbol = cc.get_symbol(to_curr)

    # Get pre and post conversion amounts
    amount_in = request['amount']
    converted_amount = cr.convert(from_curr, to_curr, Decimal(amount_in))
    converted_amount = format(converted_amount, '.2f')

    # Bundle data up in dictionary for ease in return and use in displaying
    conversion = {'from_curr': from_curr, 'to_curr': to_curr, 'amount_in': amount_in,
                  'converted_amount': converted_amount, 'in_symbol': in_symbol, 'converted_symbol': converted_symbol}

    return conversion
