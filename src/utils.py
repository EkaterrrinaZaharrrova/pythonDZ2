import json
import logging
from typing import Any

from config import ROOT_DIR
from src.external_api import get_convert_currency

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"{ROOT_DIR}/logs/{__name__}.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(module)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_json_file(filename: str = "") -> list:
    """Функция чтения JSON-файла"""
    logger.info("Начало работы.")
    try:
        data_json = json.load(open(filename, "r"))
        logger.info("Успешно!")
        return list(data_json)
    except Exception as er:
        logger.error(f"Ошибка {er}")
        return []


def transactions(operations: list[dict]) -> Any:
    """Возвращает сумму транзакции из списка.
    Транзакции в другой валюте обрабатываются через API-запрос."""
    logger.info("Начало работы.")
    try:
        for elem in operations:
            if not len(elem):
                continue

            if elem["operationAmount"]["currency"]["code"] == "RUB":
                logger.info("Успешно!")
                return float(elem["operationAmount"]["amount"])
            else:
                logger.info("Успешно!")
                return get_convert_currency(
                    elem["operationAmount"]["amount"], elem["operationAmount"]["currency"]["code"]
                )

    except Exception as er:
        logger.error(f" Ошибка {er}")
