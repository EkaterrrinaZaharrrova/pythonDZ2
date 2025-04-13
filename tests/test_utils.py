import json
import os.path

from config import ROOT_DIR
from src.utils import read_json_file, transactions


def test_empty_transactions():
    """Проверка работы в обычном режиме.
    Файл json без ошибок и верной кодировки."""

    assert transactions([{}, {}]) is None


def test_transactions() -> None:
    assert (
        transactions(
            [
                {
                    "id": 441945886,
                    "state": "EXECUTED",
                    "date": "2019-08-26T10:50:58.294041",
                    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "to": "Счет 64686473678894779589",
                }
            ]
        )
        == 31957.58
    )


def test_normal_read_json():
    """Проверка работы в обычном режиме.
    Тестовый файл json без ошибок и верной кодировки."""

    with open(ROOT_DIR + "/data/operations.json", mode="r") as preston:
        remi = json.load(preston)
    assert read_json_file(os.path.join(ROOT_DIR, "data", "operations.json")) == remi


def test_digits():
    """Файл с числами (int)."""
    assert read_json_file("test.json") == []


def test_file_not_found():
    """Несуществующий файл."""

    assert read_json_file(ROOT_DIR + "/data/test_not_found.json") == []
