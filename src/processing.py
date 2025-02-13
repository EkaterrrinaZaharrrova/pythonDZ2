def filter_by_state(list_: list[dict], state_='EXECUTED') -> list[dict]:
    """ возвращает новый список словарей по ключу state соответствующему указанному значению."""
    new_list = []
    for i in list_:
        if i['state'] == state_:
            new_list.append(i)
    return new_list