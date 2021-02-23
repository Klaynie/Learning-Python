from enum import IntEnum
import requests
import json


class ReturnCurrencies(IntEnum):
    DOLLAR = 0
    EURO = 1


class RequestUrls(IntEnum):
    FLOATRATES = 0


class ReturnFormats(IntEnum):
    JSON = 0


return_currencies = [
    'usd',
    'eur'
]


request_urls = [
    'http://www.floatrates.com/daily/'
]


return_formats = [
    '.json'
]


def get_user_input(prompt=''):
    return input()


def is_valid_user_input(input_in):
    return len(input_in) == 3


def convert_user_input(input_in):
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


def extract_currency_results(request_in):
    result = []
    json_data = request_in.json()
    for i in range(0, len(return_currencies)):
        currency = return_currencies[i]
        result.append(json_data[currency])
    return result


def print_results(result_in):
    print(result_in[ReturnCurrencies.DOLLAR])
    print(result_in[ReturnCurrencies.EURO])


def main():
    result = ''
    request_currency = get_user_input()
    if is_valid_user_input(request_currency):
        request_currency = convert_user_input(request_currency)
        request_url = create_request_url(request_currency)
        request = fetch_json(request_url)
        if is_valid_request(request):
            result = extract_currency_results(request)
    print_results(result)


main()
