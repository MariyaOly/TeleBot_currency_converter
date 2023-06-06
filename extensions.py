import requests
from config import keys
import json


class APIException(Exception):
    pass


values = {
    "Euro": "EUR",
    "US Dollar": "USD",
    "Russian Ruble": "RUB",
    "Indian Rupee": "INR",
}


class CryptoConverter:
    @staticmethod
    def convert(base: str, quote: str, amount: str):

        if base == quote:
            raise APIException(f'Unable to convert identical currencies: {base}-{quote}')

        try:
            base_ticker = values[base]
        except KeyError:
            raise APIException(f'Unable to process currency: {base}')

        try:
            quote_ticker = values[quote]
        except KeyError:
            raise APIException(f'Unable to process currency: {quote}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Unable to process amount: {amount}')

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}")
        result = json.loads(r.content)[values[quote]]
        result *= amount

        return result
