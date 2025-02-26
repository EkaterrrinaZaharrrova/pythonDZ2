from datetime import datetime
from multiprocessing.managers import Value

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_card_or_account: str) -> str:
    """Возвращать строку с замаскированным номером."""
    number_split = number_card_or_account.split()

    if "Счет" in number_split:
        account = number_split[1]
        mask_account = get_mask_account(account)
        return f"Счет {mask_account}"
    else:
        name_card = []
        mask_card = ""
        if len(number_split) > 0:
            for i in number_split:
                if i.isalpha():
                    name_card.append(i)
                elif i.isdigit():
                    mask_card = get_mask_card_number(i)
            return f"{" ".join(name_card)} {mask_card}"
        else:
            return 'Неверный ввод данных'


def get_date(date: str) -> str:
    """Возвращает форматированную строку с датой"""
    try:
        date_time = datetime.fromisoformat(date)
    except ValueError:
        return 'Неверный ввод даты'
    else:
        return date_time.strftime("%d.%m.%Y")
