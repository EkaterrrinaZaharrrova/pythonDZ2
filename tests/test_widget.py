import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "number_card_or_account, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ],
)
def test_mask_account_card(number_card_or_account, expected):
    assert mask_account_card(number_card_or_account) == expected


@pytest.mark.parametrize(
    "number_card_or_account_wrong, expected",
    [
        ("Maestro 15968378687051", "Maestro Неверный номер карты"),
        ("Счет 64686473678894779", "Счет Неверный номер счета"),
        ("", "Неверный ввод данных"),
        ("123", " Неверный номер карты"),
    ],
)
def test_mask_account_card_wrong(number_card_or_account_wrong, expected):
    assert mask_account_card(number_card_or_account_wrong) == expected


@pytest.mark.parametrize(
    "date, expected", [("2024-03-11T03:26:18.671407", "11.03.2024"), ("2024-05-15T02:56:18.671407", "15.05.2024")]
)
def test_get_date(date, expected):
    assert get_date(date) == expected


@pytest.mark.parametrize("date_wrong, expected", [("", "Неверный ввод даты"), ("06.12.2001", "Неверный ввод даты")])
def test_get_date_wrong(date_wrong, expected):
    assert get_date(date_wrong) == expected
