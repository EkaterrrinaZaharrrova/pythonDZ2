import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "currency, expected", [
        ("USD", 939719570),
        ("RUB", 873106923)
    ]
)
def test_filter_by_currency(currency, expected, transactions):
    result = filter_by_currency(transactions, currency)
    assert next(result)['id'] == expected


def test_filter_by_currency_wrong(transactions):
    result = filter_by_currency(transactions, 'EUR')
    assert next(result) is None


def test_filter_by_currency_empty_list():
    result = filter_by_currency([])
    assert next(result) is None


def test_transaction_descriptions(transactions):
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == 'Перевод организации'
    assert next(descriptions) == 'Перевод со счета на счет'


def test_transaction_descriptions_empty_list():
    descriptions = transaction_descriptions([])
    assert next(descriptions) is None


def test_card_number_generator():
    number = card_number_generator(7, 11)
    assert next(number) == '0000 0000 0000 0007'
    assert next(number) == '0000 0000 0000 0008'
    assert next(number) == '0000 0000 0000 0009'
    assert next(number) == '0000 0000 0000 0010'
    assert next(number) == '0000 0000 0000 0011'


def test_card_number_generator_max():
    number = card_number_generator(9999999999999996, 9999999999999999)
    assert next(number) == '9999 9999 9999 9996'
    assert next(number) == '9999 9999 9999 9997'
    assert next(number) == '9999 9999 9999 9998'
    assert next(number) == '9999 9999 9999 9999'
