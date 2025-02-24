import pytest

from src.masks import get_mask_card_number


#@pytest.fixture
#def number_card():
#    return ('1234567890123456')

@pytest.mark.parametrize('number_card, expected',[
    ('1234567890123456','1234 56** **** 3456'),
    ('4567456745674567', '4567 45** **** 4567')
])


def test_mask_card_number(number_card, expected):
    assert get_mask_card_number (number_card) == expected