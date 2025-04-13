import logging

from config import ROOT_DIR

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"{ROOT_DIR}/logs/{__name__}.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(module)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(number_card: str) -> str:
    """принимает на вход номер карты в виде числа и возвращает маску номера"""
    if number_card.isdigit():
        if len(number_card) == 16:
            string = number_card[:4] + " " + number_card[4:6] + "** **** " + number_card[-4:]
            logger.info("number_card -> success")
            return string
        else:
            logger.error(f"Invalid length card number: len = {len(number_card)} waiting for 16")
            return "Неверный номер карты"
    else:
        logger.error("Invalid card format")
        return "Неверный номер карты"


def get_mask_account(account: str) -> str:
    """принимает на вход номер счета в виде числа и возвращает маску номера"""
    if account.isdigit():
        if len(account) == 20:
            string = "**" + account[-4:]
            logger.info("account -> success")
            return string
        else:
            logger.error(f"Invalid length card number: len = {len(account)} waiting for 20")
            return "Неверный номер счета"
    else:
        logger.error("Invalid account format")
        return "Неверный номер счета"
