from src.widget import get_date, mask_account_card

if __name__ == "__main__":
    test1 = mask_account_card("Maestro 1596837868705199")
    test2 = mask_account_card("Счет 64686473678894779589")
    test3 = mask_account_card("Visa Platinum 8990922113665229")
    print(test1)
    print(test2)
    print(test3)

    test4 = get_date("2024-03-11T02:26:18.671407")
    print(test4)
