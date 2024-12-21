from typing import Union


def get_mask_card_number(card_num: Union[str]) -> Union[str]:
    """Функция принимает на вход номер карты и возвращает её маску"""
    return f"{card_num[:4]} {card_num[4:6]}** **** {card_num[-4:]}"


def get_mask_account(card_num_1: Union[str]) -> Union[str]:
    """Функция принимает на вход номер счёта и возвращает его маску"""
    return f"**{card_num_1[-4:]}"
