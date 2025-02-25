import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize('number_card, expected',[
    ('1234567890123456','1234 56** **** 3456'),
    ('4567456745674567', '4567 45** **** 4567')
])


def test_mask_card_number(number_card, expected):
    assert get_mask_card_number (number_card) == expected


@pytest.mark.parametrize('number_card_wrong, expected',[
    ('12345678901234','Неверный номер карты'),
    ('456745674567456797', 'Неверный номер карты'),
    ('', 'Неверный номер карты'),
    ('Visa', 'Неверный номер карты')
])


def test_mask_card_number_wrong(number_card_wrong, expected):
    assert get_mask_card_number (number_card_wrong) == expected


@pytest.mark.parametrize('account, expected',[
    ('12345678901234567890','**7890'),
    ('45674567456745674567', '**4567')
])


def test_get_mask_account(account, expected):
    assert get_mask_account (account) == expected



@pytest.mark.parametrize('account_wrong, expected',[
    ('1234567890123456','Неверный номер счета'),
    ('456745674567456745674567', 'Неверный номер счета'),
    ('', 'Неверный номер счета'),
    ('account', 'Неверный номер счета')
])


def test_get_mask_account(account_wrong, expected):
    assert get_mask_account (account_wrong) == expected