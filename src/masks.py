from typing import Union


def get_mask_card_number(to_mask: Union[str]) -> Union[str]:
    """Функция принимает на вход номер карты и возвращает её маску"""
    return f"{to_mask[:4]} {to_mask[4:6]}** **** {to_mask[-4:]}"


def get_mask_account(to_mask_card: Union[str]) -> Union[str]:
    """Функция принимает на вход номер счёта и возвращает его маску"""
    return f"**{to_mask_card[-4:]}"
