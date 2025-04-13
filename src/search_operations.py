import re
from collections import Counter


def filter_by_word(transaction: list[dict], word: str) -> list[dict]:
    """Функция поиска по регулярному выражению в описании транзакции"""
    filter_data = [data for data in transaction if re.search(word.lower(), data.get("description", "").lower())]
    return filter_data


def count_category(transaction: list[dict], category: list) -> dict:
    """Функция подсчета количества операций по категориям"""
    result_transaction = [
        data["description"] for data in transaction if data["description"] in list(map(lambda x: x, category))
    ]
    count_by_category = dict(Counter(result_transaction))
    return count_by_category
