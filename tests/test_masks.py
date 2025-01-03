from typing import Union

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "to_mask, expected", [("8675874657756475", "8675 87** **** 6475"), ("7000792289606361", "7000 79** **** 6361")]
)
def test_get_mask_card_number(to_mask, expected: Union[str]) -> None:
    assert get_mask_card_number(to_mask) == expected


def test_get_mask_card_number_negative() -> None:
    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number("")
    assert str(exc_info.value) == "Отсутствует обязательный аргумент при вводе номера карты"


def test_mask_card_number_negative(to_mask: str) -> None:
    with pytest.raises(IndexError) as exc_info:
        get_mask_card_number("32421342345534534534545345")
    assert str(exc_info.value) == "Не соответствует длина строки номера карты"


def test_get_mask_account(to_mask_card: str) -> None:
    assert get_mask_account(to_mask_card) == "**4305"


def test_get_mask_account_negative() -> None:
    with pytest.raises(TypeError) as exc_info:
        get_mask_account("")
    assert str(exc_info.value) == "Отсутствует обязательный аргумент при вводе номера счёта"


def test_mask_account_negative(to_mask_card: str) -> None:
    with pytest.raises(IndexError) as exc_info:
        get_mask_account("3242134234553453453454545455345")
    assert str(exc_info.value) == "Не соответствует длина строки номера счёта"
