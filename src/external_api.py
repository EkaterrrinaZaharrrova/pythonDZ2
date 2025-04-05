import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv(".env")
API_KEY = os.getenv("API_KEY")


def get_convert_currency(amount: float, currency: str) -> Any:
    """Принимает сумму транзакции и её валюту.
    Возвращает сумму, по актуальному курсу в указанной валюте."""

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

    headers = {"apikey": API_KEY}

    response = requests.get(url, headers=headers)

    return response.json()["result"]
