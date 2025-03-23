def get_mask_card_number(number_card: str) -> str:
    """принимает на вход номер карты в виде числа и возвращает маску номера"""
    if number_card.isdigit():
        if len(number_card) == 16:
            string = number_card[:4] + " " + number_card[4:6] + "** **** " + number_card[-4:]
            return string
        else:
            return "Неверный номер карты"
    else:
        return "Неверный номер карты"


def get_mask_account(account: str) -> str:
    """принимает на вход номер счета в виде числа и возвращает маску номера"""
    if account.isdigit():
        if len(account) == 20:
            string = "**" + account[-4:]
            return string
        else:
            return "Неверный номер счета"
    else:
        return "Неверный номер счета"
