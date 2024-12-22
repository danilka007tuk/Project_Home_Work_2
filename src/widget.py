from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_num: str) -> str:
    """Функция принимает на вход номер карты, счёта и возвращает её маску"""
    if len(card_num.split()[-1]) == 16:
        new_card = get_mask_card_number(card_num.split()[-1])
        result = f"{card_num[:-16]}{new_card}"
    elif len(card_num.split()[-1]) == 20:
        new_card = get_mask_account(card_num.split()[-1])
        result = f"{card_num[:-20]}{new_card}"
    return result


def get_new_data(old_data: str) -> str:
    """Функция принимает строку и возвращает в формате ДД.ММ.ГГГГ"""

    data_slize = old_data[0:10].split("-")
    return ".".join(data_slize[::-1])
