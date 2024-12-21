from src.masks import get_mask_account, get_mask_card_number

card_num = input("Введите номер карты: ")
print(get_mask_card_number(card_num))


card_num_1 = input("Введите номер счёта: ")
print(get_mask_account(card_num_1))
