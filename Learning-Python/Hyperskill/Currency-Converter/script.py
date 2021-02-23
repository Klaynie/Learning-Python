from enum import IntEnum
import requests


class InitialCacheCurrencies(IntEnum):
    DOLLAR = 0
    EURO = 1


class RequestUrls(IntEnum):
    FLOATRATES = 0


class ReturnFormats(IntEnum):
    JSON = 0


class CacheOutputs(IntEnum):
    CHECK_CACHE = 0
    CACHE_FOUND = 1
    CACHE_NOT_FOUND = 2


class CurrencySymbolLength(IntEnum):
    CURRENCY_LENGTH = 0


class JsonEntries(IntEnum):
    RATE = 0


initial_cache_currencies = [
    'usd',
    'eur'
]


request_urls = [
    'http://www.floatrates.com/daily/'
]


return_formats = [
    '.json'
]

user_outputs = [
    'Checking the cache…',
    'Oh! It is in the cache!',
    'Sorry, but it is not in the cache!'
]

currency_symbol_length = [
    3
]

json_entries = [
    'rate'
]


def get_user_input(prompt=''):
    return input()


def is_valid_currency_input(currency_in):
    return len(currency_in) == currency_symbol_length[CurrencySymbolLength.CURRENCY_LENGTH]


def convert_currency_input(input_in):
    return input_in.lower()


def create_request_url(input_in):
    result = request_urls[RequestUrls.FLOATRATES] \
        + input_in \
        + return_formats[ReturnFormats.JSON]
    return result


def fetch_json(url_in):
    return requests.get(url_in)


def is_valid_request(request_in):
    return True if request_in else False


def initial_cache(request_in, currency_in):
    result = {}
    json_data = request_in.json()
    if currency_in == initial_cache_currencies[InitialCacheCurrencies.DOLLAR]:
        result = update_cache(
            result, request_in, initial_cache_currencies[InitialCacheCurrencies.EURO])
    elif currency_in == initial_cache_currencies[InitialCacheCurrencies.EURO]:
        result = update_cache(
            result, request_in, initial_cache_currencies[InitialCacheCurrencies.DOLLAR])
    else:
        for i in range(0, len(initial_cache_currencies)):
            currency = initial_cache_currencies[i]
            result[currency] = json_data[currency]
    return result


def is_in_cache(cache, currency_in):
    result = True
    try:
        cache[currency_in]
    except KeyError:
        result = False
    return result


def update_cache(cache, request_in, currency_in):
    result = cache
    json_data = request_in.json()
    result[currency_in] = json_data[currency_in]
    return result


def is_valid_amount_input(amount_in):
    result = True
    try:
        float(amount_in)
    except ValueError:
        result = False
    return result


def convert_currency(cache, currency_in, amount_in):
    conversion_rate = cache[currency_in][json_entries[JsonEntries.RATE]]
    result = amount_in * conversion_rate
    return result


def print_results(amount_in, currency_in):
    print(f"You received {amount_in:.2f} {currency_in.upper()}.")


def main():
    input_currency = convert_currency_input(get_user_input())
    output_currency = convert_currency_input(get_user_input())
    input_amount = get_user_input()
    cache = {}
    keep_going = True

    if is_valid_currency_input(input_currency):
        cache_request_url = create_request_url(input_currency)
        request = fetch_json(cache_request_url)
        if is_valid_request(request):
            cache = initial_cache(request, input_currency)
            while keep_going:
                if is_valid_currency_input(output_currency):
                    print(user_outputs[CacheOutputs.CHECK_CACHE])
                    if not is_in_cache(cache, output_currency):
                        print(user_outputs[CacheOutputs.CACHE_NOT_FOUND])
                        cache = update_cache(cache, request, output_currency)
                    else:
                        print(user_outputs[CacheOutputs.CACHE_FOUND])

                if is_valid_amount_input(input_amount):
                    input_amount = float(input_amount)
                    output_amount = convert_currency(
                        cache, output_currency, input_amount)

                print_results(output_amount, output_currency)
                output_currency = convert_currency_input(get_user_input())
                if len(output_currency) == 0:
                    keep_going = False
                    break
                input_amount = convert_currency_input(get_user_input())


main()
