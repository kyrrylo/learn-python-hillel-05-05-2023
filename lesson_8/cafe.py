MENU = {
    "Американо": 20,
    "Эспрессо": 15,
    "Раф": 25,
    "Чай альпийские луга": 13.5,
    "Чай черный травяной альпийские луга": 135,
    "Чай зелёный": 13,
    "Круассан": 20,
    "Пончик": 18,
    "Пирожок": 15,
}


def display_menu():
    """
    Функция красиво и презентабельно выводит на экран меню заведения
    """
    # pass можно вставлять после любого отступа как "затычку" для еще ненаписанного кода
    # позволяет программе выполняться без ошибок когда там еще не закончено заполнение логики
    # https://pyformat.info/
    # '{:10} {:20}'.format(test1, test2)
    # то же, что и ниже
    # f'{test1:10} {test2:20}'
    for key, value in MENU.items():
        # print('{:20}'.format(key), value)
        print(f'{key:20} - {value}')


# -> <data type> означает тип возвращаемых данных этой функцией
def get_user_menu_choice() -> str:
    """
    Выясняет что пользователь хочет заказать
    :return: выбор пользователя, который есть в меню
    """
    user_order = input('Что хотите заказать? ')
    while user_order not in MENU:
        print('К сожалению, у нас такого нет, выберите что-нибудь другое')
        # display_menu()
        user_order = input('Что хотите заказать? ')
    return user_order


def order_menu_item(user_money: float):
    """
    Функция отвечает за построение диалога с пользователем
    Проверяет может ли пользователь это оплатить
    Выдать заказ и вернуть сдачу
    :return:
    """
    display_menu()
    # одинаковые имена переменных внутри разных функций могут быть
    # а одинаковые имена переменных внутри функции и __main__ кода - не могут (вернее, настоятельно не рекомендуются)
    user_order = get_user_menu_choice()
    if MENU[user_order] <= user_money:
        print(f'Пожалуйста, вот ваш {user_order}')
        return user_money - MENU[user_order]
    else:
        print(f'{user_order} стоит {MENU[user_order]}, у вас только {user_money}!')
        return user_money


if __name__ == '__main__':
    pocket_money = 100
    pocket_money = order_menu_item(pocket_money)

    print(f'Поход в кафе завершён, у нас осталось {pocket_money}')
