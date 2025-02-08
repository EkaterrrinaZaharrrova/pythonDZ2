from src.masks import get_mask_account, get_mask_card_number
from datetime import datetime


def mask_account_card(number_card_or_account: str) -> str:
    """ Возвращать строку с замаскированным номером."""
    number_split = number_card_or_account.split()

    if "Счет" in number_split:
        account = number_split[1]
        mask_account = get_mask_account(account)
        return f"Счет {mask_account}"
    else:
        name_card = []
        mask_card = ""
        for i in number_split:
            if i.isalpha():
                name_card.append(i)
            elif i.isdigit():
                mask_card = get_mask_card_number(i)
        return f"{" ".join(name_card)} {mask_card}"


def get_date(date: str) -> str:
    """возвращает форматированную строку с датой"""
    date_time = datetime.fromisoformat(date)
    return date_time.strftime("%d.%m.%Y")
