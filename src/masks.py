from typing import Union


def get_mask_card_number(to_mask: Union[str]) -> Union[str]:
    """Функция принимает на вход номер карты и возвращает её маску"""
    if to_mask == "":
        raise TypeError("Отсутствует обязательный аргумент при вводе номера карты")
    elif len(to_mask) != 16:
        raise IndexError("Не соответствует длина строки номера карты")
    return f"{to_mask[:4]} {to_mask[4:6]}** **** {to_mask[-4:]}"


def get_mask_account(to_mask_card: Union[str]) -> Union[str]:
    """Функция принимает на вход номер счёта и возвращает его маску"""
    if to_mask_card == "":
        raise TypeError("Отсутствует обязательный аргумент при вводе номера счёта")
    elif len(to_mask_card) != 20:
        raise IndexError("Не соответствует длина строки номера счёта")
    return f"**{to_mask_card[-4:]}"
