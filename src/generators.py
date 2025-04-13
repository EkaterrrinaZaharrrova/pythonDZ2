from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str = None) -> Generator:
    """Поочередно выдает транзакции, где валюта операции соответствует заданной"""
    return (transaction for transaction in transactions if
            transaction.get("operationAmount", {}).get("currency", {}).get("code", "") == currency
            or transaction.get("currency_code", {}) == currency
            )


def transaction_descriptions(transactions: list[dict]) -> str:
    """Возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield (transaction["description"])

    while True:
        yield None


def card_number_generator(start: int, stop: int) -> str:
    """выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    while True:
        num = str(start).zfill(16)
        result = num[0:4] + " " + num[4:8] + " " + num[8:12] + " " + num[12:]
        yield result
        if start == stop:
            break
        start += 1
