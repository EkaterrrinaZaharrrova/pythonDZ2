import json

def read_json_file(filename: str = "") -> list:
    """Функция чтения JSON-файла"""
    try:
        data_json = json.load(open(filename, "r"))
        return list(data_json)
    except Exception:
        return []