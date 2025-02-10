from src.search_str_description import count_transactions_by_category, filter_transactions


def test_count_transactions_by_category():
    transactions = [
        {"description": "Перевод с карты на карту", "amount": 1000, "currency": "RUB"},
        {"description": "Открытие вклада", "amount": 5000, "currency": "RUB"},
        {"description": "Перевод на счет", "amount": 2000, "currency": "USD"},
    ]
    categories = ["перевод", "вклад"]
    result = count_transactions_by_category(transactions, categories)
    assert result["вклад"] == 1
    assert result["перевод"] == 2


def test_count_transactions_by_category_empty():
    transactions = [
        {"description": "Перевод с карты на карту", "amount": 1000, "currency": "RUB"},
        {"description": "Открытие вклада", "amount": 5000, "currency": "RUB"},
    ]
    categories = ["отсутствует данная категория"]
    result = count_transactions_by_category(transactions, categories)
    assert result["отсутствует данная категория"] == 0


def test_filter_transactions():
    transactions = [
        {"description": "Перевод с карты на карту", "amount": 1000, "currency": "RUB"},
        {"description": "Открытие вклада", "amount": 5000, "currency": "RUB"},
        {"description": "Перевод на счет", "amount": 2000, "currency": "USD"},
    ]
    search_string = "вклад"
    result = filter_transactions(transactions, search_string)
    assert len(result) == 1
    assert result[0]["description"] == "Открытие вклада"
