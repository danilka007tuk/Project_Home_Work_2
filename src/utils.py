import json
import os
from pathlib import Path
from typing import Any

from src.logging import get_logger

# logger = logging.getLogger(__name__)
# log_path ="./logs/utils.log"
# log_path = "." + log_path
# file_handler = logging.FileHandler(log_path, "w+")
# file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
# file_handler.setFormatter(file_formatter)
# logger.addHandler(file_handler)
# logger.setLevel(logging.DEBUG)

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "../logs", "utils.log")
logger = get_logger("utils", file_path_1)


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"


def operation(open_file: Any) -> Any:
    """Принимает на вход имя JSON-файла по пути ./data/ и
    возвращает список словарей с данными о финансовых транзакциях"""
    open_file += ".json"
    try:
        logger.info(
            f"Данная функция {operation.__name__} принимает на вход имя JSON-файла и возвращает список словарей"
        )
        with open(DATA_DIR / open_file, "r", encoding="utf-8") as jf:
            data = json.load(jf)
    except Exception as e:
        logger.error(f"Произошла ошибка типа {e}")
        print(f"Ошибка {e}")
        return []
    except FileNotFoundError as e:
        logger.error(f"Произошла ошибка типа {e}")
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
