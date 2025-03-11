from datetime import datetime


def filter_by_state(input_list: list[dict], state_: str = 'EXECUTED') -> list[dict]:
    """ возвращает новый список словарей по ключу state соответствующему указанному значению."""
    sort_list_state = []
    if len(input_list) > 0:
        for i in input_list:
            if i['state'] == state_:
                sort_list_state.append(i)
    return sort_list_state


def sort_by_date(input_list: list[dict], reverse_: bool = True) -> list[dict]:
    """ возвращает новый список, отсортированный по дате"""
    try:
        sort_list_data = sorted(
            input_list,
            key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=reverse_)
    except ValueError:
        return 'Неверный формат даты'
    else:
        return sort_list_data
