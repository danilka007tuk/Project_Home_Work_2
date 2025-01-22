import json
from pathlib import Path
from typing import Any

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"


def operation(open_file: Any) -> Any:
    """Принимает на вход имя JSON-файла по пути ./data/ и
    возвращает список словарей с данными о финансовых транзакциях"""
    open_file += ".json"
    try:
        with open(DATA_DIR / open_file, "r", encoding="utf-8") as jf:
            data = json.load(jf)
    except Exception as e:
        print(f"Ошибка {e}")
        return []
    except FileNotFoundError as e:
        print(f"Ошибка {e}")
        return []
    return data


#
# def operation(filename="data/operations.json") -> list:
#     """Функция принимает json возвращает list или dict"""
#     try:
#         with open(filename, "r") as file:
#             data = json.load(file)
#     except Exception as e:
#         print(f"Ошибка {e}")
#         return []
#     except FileNotFoundError as e:
#         print(f"Ошибка {e}")
#         return []
#     return data
