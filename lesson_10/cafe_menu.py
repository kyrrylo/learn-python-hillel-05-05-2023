STARTING_MENU = {
    "Американо": {
        "price": 20,
        "quantity": 50,
    },
    "Эспрессо": {
        "price": 15,
        "quantity": 50,
    },
    "Раф": {
        "price": 25,
        "quantity": 30,
    },
    "Чай альпийские луга": {
        "price": 13.5,
        "quantity": 50,
    },
    "Чай черный травяной альпийские луга": {
        "price": 135,
        "quantity": 50,
    },
    "Чай зелёный": {
        "price": 13,
        "quantity": 50,
    },
    "Круассан": {
        "price": 20,
        "quantity": 5,
    },
    "Пончик": {
        "price": 18,
        "quantity": 1,
    },
    "Пирожок": {
        "price": 15,
        "quantity": 0,
    },
}


def display_menu(menu: dict):
    """
    Функция красиво и презентабельно выводит на экран меню заведения
    :param menu: меню заведения в формате словаря
    """
    # pass можно вставлять после любого отступа как "затычку" для еще ненаписанного кода
    # позволяет программе выполняться без ошибок когда там еще не закончено заполнение логики
    # https://pyformat.info/
    # '{:10} {:20}'.format(test1, test2)
    # то же, что и ниже
    # f'{test1:10} {test2:20}'
    for key, value in menu.items():
        # print('{:20}'.format(key), value)
        if value["quantity"] > 0:
            print(f'{key:20} - {value["price"]}')