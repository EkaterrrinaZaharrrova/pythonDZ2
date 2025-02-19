from datetime import datetime


def filter_by_state(list_: list[dict], state_='EXECUTED') -> list[dict]:
    """ возвращает новый список словарей по ключу state соответствующему указанному значению."""
    new_list = []
    for i in list_:
        if i['state'] == state_:
            new_list.append(i)
    return new_list


def sort_by_date(list_: list[dict], reverse_='True') -> list[dict]:
    """ возвращает новый список, отсортированный по дате"""
    new_list = sorted(
        list_,
        key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=reverse_)
    return new_list
