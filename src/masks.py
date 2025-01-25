import logging
from typing import Union

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/mask.log", "w+")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(to_mask: Union[str]) -> Union[str]:
    """Функция принимает на вход номер карты и возвращает её маску"""
    logger.info(f"Данная функция {get_mask_card_number.__name__} маскирует номер карты по типу 1234 56** **** 4567")
    if to_mask == "":
        logger.error(f"Произошла ошибка типа {TypeError}: отсутствует аргумент ввода")
        raise TypeError("Отсутствует обязательный аргумент при вводе номера карты")
    elif len(to_mask) != 16:
        logger.error(f"Произошла ошибка типа {IndexError}: не соответствует длина строки аргументы ввода")
        raise IndexError("Не соответствует длина строки номера карты")
    return f"{to_mask[:4]} {to_mask[4:6]}** **** {to_mask[-4:]}"


def get_mask_account(to_mask_card: Union[str]) -> Union[str]:
    """Функция принимает на вход номер счёта и возвращает его маску"""
    logger.info(f"Данная функция {get_mask_account.__name__} маскирует номер счёта по типу **1234")
    if to_mask_card == "":
        logger.error(f"Произошла ошибка типа {TypeError}: отсутствует аргумент ввода")
        raise TypeError("Отсутствует обязательный аргумент при вводе номера счёта")
    elif len(to_mask_card) != 20:
        logger.error(f"Произошла ошибка типа {IndexError}: не соответствует длина строки аргументы ввода")
        raise IndexError("Не соответствует длина строки номера счёта")
    return f"**{to_mask_card[-4:]}"
