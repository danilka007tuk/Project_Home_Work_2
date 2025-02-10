import csv
import json
from datetime import datetime
from typing import Any

import pandas as pd


"""Этот модуль создан для функционала функции main в модуле main_3
Он включает в себя подобие функции ранее реализованных в проекте для поддержания корректного функционала 
функций и их тестов"""


def read_json(json_file: str) -> list[dict | None]:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        return []
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        return []
    if not isinstance(data, list):
        return []

    return data


def read_csv(csv_file: str) -> list:
    """Принимает на вход путь до CSV-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open(csv_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            data = list(reader)
    except FileNotFoundError:
        return []
    if not data:
        return []
    if not isinstance(data, list):
        return []

    return data


def read_excel(xlsx_file: str) -> list:
    """Принимает на вход путь до XLSX-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        excel_data = pd.read_excel(xlsx_file).to_dict(orient="records")
    except FileNotFoundError:
        return []
    if not excel_data:
        return []
    if not isinstance(excel_data, list):
        return []

    return excel_data


def read_file(file_path: str) -> list[dict | None]:
    *file_name, file_extension = file_path.split(".")
    content: list = []
    match file_extension:
        case "json":
            content = read_json(file_path)
        case "csv":
            content = read_csv(file_path)
        case "xlsx":
            content = read_excel(file_path)
    return content


def filter_by_state_1(transactions_list: list, state: str = "EXECUTED") -> list:
    """Функция возвращает список словарей, содержащий только те словари, у которых ключ 'state' соответствует\
    указанному значению в параметре state."""
    if not transactions_list:
        raise ValueError("Список операций не должен быть пустым!")
    result = []
    for transaction in transactions_list:
        if transaction == {}:
            continue
        if transaction["state"] == state:
            result.append(transaction)
    return result


def sort_by_date_1(transactions_list: list, sorting_order: int | bool = 1) -> list:
    """Функция возвращает новый список, отсортированный по дате."""
    if not transactions_list:

        raise ValueError("Список операций не должен быть пустым!")

    # Преобразуем строки дат в объекты datetime для корректной сортировки
    def get_date_key(transaction: dict[str, Any]) -> datetime:
        date_str = transaction.get("date")  # Получаем значение даты
        if isinstance(date_str, str) and len(date_str) >= 10:  # Проверяем, что это строка и она достаточно длинная
            try:
                return datetime.strptime(date_str[:10], "%Y-%m-%d")
            except ValueError:
                return datetime.min  # Возвращаем минимальную дату, если формат неверный
        return datetime.min  # Возвращаем минимальную дату, если дата отсутствует или не строка

    try:
        sorted_transactions = sorted(
            transactions_list,
            key=get_date_key,
            reverse=sorting_order == 0,  # Если sorting_order 0, сортируем по возрастанию
        )
    except Exception as e:
        raise e
    return sorted_transactions


def filter_by_rub_json(transactions_list: list) -> list:
    """Функция возвращает список словарей, содержащий только те словари, у которых ключ 'code' равен RUB."""
    if not transactions_list:
        raise ValueError("Список операций не должен быть пустым!")

    result = []
    for transaction in transactions_list:
        if transaction == {}:
            continue
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            result.append(transaction)
    return result


def filter_by_rub_cvs_xlsx(transactions_list: list) -> list:
    """Функция возвращает список словарей, содержащий только те словари, у которых ключ 'code' равен RUB."""
    if not transactions_list:
        raise ValueError("Список операций не должен быть пустым!")

    result = []
    for transaction in transactions_list:
        if transaction == {}:
            continue
        if transaction["currency_code"] == "RUB":
            result.append(transaction)
    return result
