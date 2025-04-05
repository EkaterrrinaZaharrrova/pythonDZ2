import json
import logging
from typing import Any

from src.external_api import get_convert_currency


def read_json_file(filename: str = "") -> list:
    """Функция чтения JSON-файла"""
    try:
        data_json = json.load(open(filename, "r"))
        return list(data_json)
    except Exception:
        return []


def transactions(operations: list[dict]) -> Any:
    """Возвращает сумму транзакции из списка.
    Транзакции в другой валюте обрабатываются через API-запрос."""

    try:
        for elem in operations:
            if not len(elem):
                continue

            if elem["operationAmount"]["currency"]["code"] == "RUB":
                return float(elem["operationAmount"]["amount"])
            else:
                return get_convert_currency(
                    elem["operationAmount"]["amount"], elem["operationAmount"]["currency"]["code"]
                )

    except Exception as er:
        logging.error(f" Ошибка {er}")
