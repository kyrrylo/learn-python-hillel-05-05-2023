from cafe_menu import MENU, display_menu


def check_menu():
    """
    Функция отвечает за проверку пунктов меню.
    Если что-то заканчивается или закончилось - требует пополнения
    :return:
    """
    for key, value in MENU.items():
        if value['quantity'] == 0:
            print(f'У нас закончились {key}!!! Нужно срочно сделать еще!')
        elif value['quantity'] < 5:
        # if 0 < value['quantity'] < 5:  # Это тоже сработает!
            print(f'У нас заканчиваются {key}. Осталось {value["quantity"]}!')


if __name__ == '__main__':
    check_menu()