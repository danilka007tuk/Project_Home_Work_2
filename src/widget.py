from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(to_mask: str) -> str:
    """Функция принимает на вход номер карты, счёта и возвращает её маску"""
    if len(to_mask.split()[-1]) == 16:
        new_card = get_mask_card_number(to_mask.split()[-1])
        result = f"{to_mask[:-16]}{new_card}"
    elif len(to_mask.split()[-1]) == 20:
        new_card = get_mask_account(to_mask.split()[-1])
        result = f"{to_mask[:-20]}{new_card}"
    elif len(get_mask_card_number(to_mask.split()[-1])) != 16:
        raise IndexError("Не соответствует длина строки номера карты")
    elif len(get_mask_account(to_mask.split()[-1])) != 20:
        raise IndexError("Не соответствует длина строки номера счёта")
    return result


def get_new_data(old_data: str) -> str:
    """Функция принимает строку и возвращает в формате ДД.ММ.ГГГГ"""
    if old_data == "":
        raise TypeError("Отсутствует обязательный аргумент")
    data_slize = old_data[0:10].split("-")
    return ".".join(data_slize[::-1])
