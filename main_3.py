from src.develop_main_3 import filter_by_rub_cvs_xlsx, filter_by_rub_json, filter_by_state_1, read_file, sort_by_date_1
from src.search_str_description import filter_transactions
from src.widget import get_new_data, mask_account_card


def main() -> None:
    """Отвечает за основную логику проекта и связывает функции между собой"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")
    choice = input("Пользователь: ")
    transactions_data = []
    match choice:
        case "1":
            print("Для обработки выбран JSON-файл.")
            transactions_data = read_file("./data/operations.json")
        case "2":
            print("Для обработки выбран CSV-файл.")
            transactions_data = read_file("./data_2/transactions.csv")
        case "3":
            print("Для обработки выбран XLSX-файл.")
            transactions_data = read_file("./data_2/transactions_excel.xlsx")

    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. "
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\nПользователь: "
        )
        if status.upper() in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f'Операции отфильтрованы по статусу "{status.upper()}"')
            filtered_transactions = filter_by_state_1(transactions_data, status)
            break
        else:
            print(f'Статус операции "{status}" недоступен.')

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return
        # Сортировка списка транзакций по дате, если пользователь выбрал этот критерий.
    do_sort_by_date = 0
    user_input = input("Отсортировать операции по дате? Да/Нет\nПользователь:")
    if user_input.lower() == "да":
        do_sort_by_date = 1
        user_input = input("Отсортировать по возрастанию (нажмите 0) или по убыванию (нажмите 1)?\nПользователь:")
        if user_input.lower() == "по возрастанию":
            sorting_order = 0
        else:
            sorting_order = 1
        if do_sort_by_date:
            transactions_data = sort_by_date_1(transactions_data, sorting_order)

    user_input = input("Выводить только рублевые транзакции? Да/Нет\nПользователь:")
    if user_input.lower() == "да":
        if choice == "1":
            transactions_data = filter_by_rub_json(transactions_data)
        else:
            transactions_data = filter_by_rub_cvs_xlsx(transactions_data)

    do_filter_by_description = 0
    user_input = input("Отфильтровать список транзакций по описанию? Да/Нет\nПользователь:")
    if user_input.lower() == "да":
        do_filter_by_description = 1

    if do_filter_by_description:
        user_input = input(
            "Какие именно операции отразить в списке транзакций?"
            "(доступно: Перевод с карты на карту, Перевод организации\n"
            "Открытие вклада, Перевод со счета на счет, Перевод с карты на счет\nПользователь:"
        )
        transactions_data = filter_transactions(transactions_data, user_input)

    if not transactions_data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")

    for transaction in transactions_data:
        if isinstance(transaction, dict):  # Проверка, является ли элемент словарем
            date = transaction.get("date")
            description = transaction.get("description")
            from_account = transaction.get("from")
            to_account = transaction.get("to")
            operation_amount = transaction.get("operationAmount")
            amount = transaction.get("amount")
            currency_name = transaction.get("currency_name")

            if date and description and to_account and from_account:  # Проверка на наличие необходимых ключей
                print(f"{get_new_data(date)} {description}")
                print(f"{mask_account_card(from_account)} -> {mask_account_card(to_account)}")
                if choice == "1":
                    if (
                        operation_amount
                        and isinstance(operation_amount, dict)
                        and "amount" in operation_amount
                        and "currency" in operation_amount
                        and isinstance(operation_amount["currency"], dict)
                        and "name" in operation_amount["currency"]
                    ):  # Многоуровневая проверка
                        print(f"{operation_amount['amount']} {operation_amount['currency']['name']}\n")
                    else:
                        print("Ошибка: Отсутствуют данные о сумме операции.")
                else:
                    if amount and currency_name:
                        print(f"Сумма: {amount} {currency_name}\n")
                    else:
                        print("Ошибка: Отсутствуют данные о сумме.")
            else:
                print("Ошибка: В транзакции отсутствуют необходимые данные (date, description, to).")
        else:
            print("Ошибка: Элемент transactions_data не является словарем.")


main()


# import sys
# from src.search_str import operation_search
# from src.utils import operation
# from src.processing import sort_by_date
# from src.generators import filter_by_currency
#
# def main():
# print(f'''Привет! Добро пожаловать в программу работы с банковскими транзакциями. Выберите необходимый пункт меню:
#     1. Получить информацию о транзакциях из JSON-файла
#     2. Получить информацию о транзакциях из CSV-файла
#     3. Получить информацию о транзакциях из XLSX-файла''')
#
#     try:
#         choice = int(input("Пользователь:"))
#         if choice not in [1, 2, 3]:
#             raise ValueError("Некорректный ввод. Выберите номер от 1 до 3.")
#
#         if choice == 1:
#             print("Для обработки выбран JSON-файл")
#             transactions_list = operation("operations")
#         elif choice == 2:
#             print("Для обработки выбран CSV-файл")
#             transactions_list = operation("csv_operations")
#         elif choice == 3:
#             print("Для обработки выбран XLSX-файл")
#             transactions_list = operation("xlsx_operations")
#
# print(''' Введите статус, по которому необходимо выполнить фильтрацию.
# Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING''')
#
#         status = input("Пользователь:").strip().upper()
#         if status not in ["EXECUTED", "CANCELED", "PENDING"]:
#             raise ValueError(f"Некорректный статус '{status}'. Доступны: EXECUTED, CANCELED, PENDING.")
#
#         filtered_transactions = operation_search(transactions_list, status)
#         print(filtered_transactions)
#
#         answer = input("Выводить только рублевые транзакции? Да/Нет ").strip().lower()
#         if answer == "да":
#             ruble_transactions = filter_by_currency(filtered_transactions, "RUB")
#             print(list(ruble_transactions))
#         else:
#             print(filtered_transactions)
#
#         answer = input("Отсортировать операции по дате? Да/Нет ").strip().lower()
#         if answer == "да":
#             sorted_transactions = sort_by_date(ruble_transactions, True)
#             print(list(sorted_transactions))
#         else:
#             print(filtered_transactions)
#
#     except ValueError as e:
#         print(f"Произошла ошибка: {e}")
#         sys.exit(1)
#
# if __name__ == "__main__":
#     main()


#
#
#
#
# def main():
#     print(f'''{main.__name__}: Привет! Добро пожаловать в программу работы с банковскими транзакциями.
#
# Выберите необходимый пункт меню:
#     1. Получить информацию о транзакциях из JSON-файла
#     2. Получить информацию о транзакциях из CSV-файла
#     3. Получить информацию о транзакциях из XLSX-файла''')
#     choice = input("Пользователь:")
#     if  choice  == "1":
#         print(f"{operation("operations")}\n{main.__name__}: Для обработки выбран JSON-файл")
#     else:
#          print("Неправильный ввод номера для получения информации по транзакциям")
#          sys.exit(1)
#     print(f'''{main.__name__}: Введите статус, по которому необходимо выполнить фильтрацию.
# Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')
#     status = input("Пользователь:").lower()
#     while True:
#         if  status == 'executed':
#             transactions_list_2 = operation("operations")
#             convert = operation_search(transactions_list_2,  'EXECUTED')
#             print(convert)
#             break
#         elif status == 'canceled':
#             transactions_list_2 = operation("operations")
#             convert = operation_search(transactions_list_2,  'CANCELED')
#             print(convert)
#             break
#         elif status == 'pending':
#             transactions_list_2 = operation("operations")
#             convert = operation_search(transactions_list_2,  'PENDING')
#             continue
#         else:
#             print(f"{main.__name__}: Статус операции {status} недоступен.")
#             print(f'''{main.__name__}: Введите статус, по которому необходимо выполнить фильтрацию.
# Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')
#             sys.exit(1)
#


# while True:
#     print(f"{main.__name__}: Выводить только рублевые транзакции? Да/Нет")
#     answer  = input("Пользователь:").lower()
#     if answer == "да":
#         convert_2 = filter_by_currency(convert, "RUB")
#         print(f"{main.__name__}: Отсортировать операции по дате? Да/Нет")
#     result = input("Пользователь:").lower()
#     if result == "да":
#         convert_3 = sort_by_date(convert_2)
#         print(convert_3)
#     elif answer != "да":
#         convert_no = filter_by_currency(convert,"")
#     elif answer != "да":
#         convert_4 = sort_by_date(convert_no)
#         print(convert_4)


#
# Пользователь: test
#
# Программа: Статус операции "test" недоступен.
#
# Программа: Введите статус, по которому необходимо выполнить фильтрацию.
# Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING


# elif result == "2":
#     file_path_1 = os.path.join("data_2", "transactions.csv")
#     print(f"{read_csv(file_path_1)}\n{main.__name__}: Для обработки выбран CSV-файл")
# elif result == "3":
#     file_path_2 = os.path.join("data_2", "transactions_excel.xlsx")
#     print(f"{read_excel(file_path_2)}\n{main.__name__}: Для обработки выбран XLSX-файл")
