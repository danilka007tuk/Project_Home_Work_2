import re
from typing import Dict, List


def filter_transactions(transactions: List[Dict], search_string: str) -> List[Dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка"""
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)  # Компилируем шаблон
    filtered_transactions = [
        transaction for transaction in transactions if pattern.search(transaction.get("description", ""))
    ]
    return filtered_transactions


def count_transactions_by_category(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории."""
    category_count = {category: 0 for category in categories}
    for transaction in transactions:
        description = transaction.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                category_count[category] += 1
    return category_count


# def search_transactions(transactions_list: list, key_string: str) -> list:
#     """Принимает список словарей с данными о банковских операциях и строку поиска. Возвращает список словарей, у \
#     которых в описании есть данная строка."""
#     templates = [
#         "перевод с карты на карту",
#         "перевод организации",
#         "перевод со счета на счет",
#         "открытие вклада",
#         "перевод с карты на счет",
#     ]
#     key_list = []
#     pattern = re.compile(key_string.lower())
#     for temp in templates:
#         if re.search(pattern, temp):
#             key_list.append(temp)
#     filtered_transactions_list = []
#     for key in key_list:
#         for transaction in transactions_list:
#             if transaction == {}:
#                 continue
#             if transaction["description"].lower() != key:
#                 continue
#             filtered_transactions_list.append(transaction)
#     return filtered_transactions_list


# import pandas as pd
# import os

# Чтение CSV-файла
# file_path_1 = os.path.join("data_2", "transactions.csv")
# bank_operations = pd.read_csv(file_path_1)
# # Указываем категории для поиска
# search_strings = ["открытие", "перевод"]
# # Подсчет количества операций по категориям
#
# def count_operations_by_category(operations, search_string):
#     result = {category: 0 for category in search_string}
#     for operation in operations:
#          if operation["description"] in search_string:
#              result[operation["description"]] += 1
#     return result
#
#
# counted_operations = count_operations_by_category(bank_operations, search_strings)
# print(counted_operations)


# from src.search_str import operation_search
# from collections import Counter

#
#
#
#
# transactions_list_2 = operation("operations")
#
#
# convert = operation_search(transactions_list_2, 'EXECUTED')
# print(convert)
#
#
#
# search_strings = ["открытие", "перевод"]
# open_file = "./data/operations.json"
#
# results = operation_search(open_file, search_strings)
#
#
# if results:
#     print(len(results))
# else:
#      print('Совпадения не найдены.')
#
#
#


# import re
# from collections import Counter
# import json
# def operation_search(transactions, query):
#     return [
#         transaction
#         for transaction in transactions
#         if "state" in transaction and re.search(query, transaction["state"], re.IGNORECASE)
#     ]

# def operation_search_description(transactions, query):
#     return [
#         transaction
#         for transaction in transactions
#         if "description" in transaction and re.search(query, transaction["description"], re.IGNORECASE)
#     ]

#
# def operation_search(open_file, search_strings):
#     with open(open_file, "r", encoding="utf-8") as file:
#         data = json.load(file)
#         result = []
#     for transaction in data:
#         if 'description' in transaction:
#  if any(re.search(search_string, transaction['description'], re.IGNORECASE) for search_string in search_strings):
#                 result.append(transaction)
#     return result


# result = []
# for transaction in data:
#     if 'description' in transaction and re.findall(search_string, transaction['description'], re.IGNORECASE):
#         result.append(transaction['description'])
#     elif 'description' in transaction and re.findall(search_string_2, transaction['description'], re.IGNORECASE):
#         result.append(transaction['description'])
#     # elif 'description' in transaction and re.findall(search_string_3, transaction['description'], re.IGNORECASE):
#     result.append(transaction['description'])
# elif 'description' in transaction and re.findall(search_string_4, transaction['description'], re.IGNORECASE):
#     result.append(transaction['description'])
# elif 'description' in transaction and re.findall(search_string_5, transaction['description'], re.IGNORECASE):
#     result.append(transaction['description'])
# return result

# json_string = json.dumps(data)
#
# pattern = f'{search_string}"'
# matches = re.findall(pattern, json_string)
#
# return matches
