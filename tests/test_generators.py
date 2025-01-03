import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(list_dict_check) -> None:
    generator = filter_by_currency(list_dict_check)
    assert next(generator)


def test_filter_by_currency_negative() -> None:
    with pytest.raises(TypeError, match="Не соответствует заданной валюте"):
        list(filter_by_currency([{"operationAmount": {"currency": {"code": ""}}}], " "))


def test_transaction_descriptions(list_dict) -> None:
    generator = transaction_descriptions(list_dict)
    assert list(generator)


def test_transaction_descriptions_negative() -> None:
    with pytest.raises(TypeError, match="Отсутствует строка"):
        list(transaction_descriptions([{"": ""}]))


def test_card_number_generator() -> None:
    generator = card_number_generator(0, 5)
    assert list(generator)


def test_card_number_generator_negative() -> None:
    with pytest.raises(IndexError, match="Неправильный ввод данных"):
        list(card_number_generator(5, 0))
