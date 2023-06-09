# from <имя файла откуда импортируем> import <через запятую имена функций/переменных,
#                                               которые нужно импортировать сюда>
from cafe_menu import STARTING_MENU, display_menu


# -> <data type> означает тип возвращаемых данных этой функцией
def get_user_menu_choice(menu: dict) -> str:
    """
    Выясняет что пользователь хочет заказать
    :param menu: меню заведения в формате словаря
    :return: выбор пользователя, который есть в меню
    """
    ask_query = 'Что хотите заказать? (напишите paybill чтобы рассчитаться и уйти) '
    user_order = input(ask_query)
    # TODO Сделать так, чтобы нельзя было заказывать то чего нет в наличии
    while (user_order not in menu) and user_order.strip() != "paybill":
        print('К сожалению, у нас такого нет, выберите что-нибудь другое')
        # display_menu()
        user_order = input(ask_query)
    return user_order


def order_menu_item(menu: dict, user_money: float):
    """
    Функция отвечает за построение диалога с пользователем
    Проверяет может ли пользователь это оплатить
    Выдать заказ и вернуть сдачу
    :param menu: меню заведения в формате словаря
    :param user_money: какую сумму "протягивает" клиент
    :return: сдачу
    """
    display_menu(menu)
    # одинаковые имена переменных внутри разных функций могут быть
    # а одинаковые имена переменных внутри функции и __main__ кода - не могут (вернее, настоятельно не рекомендуются)
    print(f"У вас {pocket_money}, можете сделать заказ")
    user_order = get_user_menu_choice(menu)
    if user_order == 'paybill':
        print(f'Благодарим вас за визит!')
        return -1
    elif menu[user_order]['price'] <= user_money:
        print(f'Пожалуйста, вот ваш {user_order}')
        menu[user_order]['quantity'] -= 1
        return user_money - menu[user_order]['price']
    else:
        print(f'{user_order} стоит {menu[user_order]["price"]}, у вас только {user_money}!')
        return user_money


if __name__ == '__main__':
    cafe_menu = STARTING_MENU.copy()
    pocket_money = 100
    while True:
        return_value = order_menu_item(cafe_menu, pocket_money)
        if return_value == -1:
            break
        else:
            pocket_money = return_value

    print(f'Поход в кафе завершён, у нас осталось {pocket_money}')

