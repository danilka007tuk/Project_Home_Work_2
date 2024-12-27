from src.widget import get_new_data, mask_account_card

if __name__ == "__main__":
    card_number = input("Введите номер карты или счёта: ")
    print(mask_account_card(card_number))

if __name__ == "__main__":
    data_number = input("Введите полную дату: ")
    print(get_new_data(data_number))
