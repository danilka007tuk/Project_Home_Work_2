import pytest

from src.widget import get_new_data, mask_account_card


def test_mask_account_card(new_card: str) -> None:
    assert mask_account_card(new_card) == "Visa Platinum 7000 79** **** 6361"


def test_mask_account_negative(new_card: str) -> None:
    with pytest.raises(IndexError) as exc_info:
        mask_account_card("32421342345534534534545345")
    assert str(exc_info.value) == "Не соответствует длина строки номера карты"


def test_get_new_data(old_data: str) -> None:
    assert get_new_data(old_data) == "11.03.2024"


def test_get_new_data_negative() -> None:
    with pytest.raises(TypeError) as exc_info:
        get_new_data("")
    assert str(exc_info.value) == "Отсутствует обязательный аргумент"
