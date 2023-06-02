def my_function():
    print('My function was called')

if __name__ == '__main__':
    # list
    # str
    # tuple
    # set
    # dict (dictionary) словарь

    d = dict()
    # {<ключ1>: <значение1>, <ключ2>: <значение2>, ...}
    d = {
        "function": my_function,
        "moon": "луна",
        "sun": "солнце",
        "can": ("могу", "уметь", "способность что-то сделать"),
        "true": True,
        "one": 1,
        "unicorn": ["what", "kind", "of", "единорог?"],
        "some set": {3, 5, True, False, 1, 18.3, "Big text"},
        (1, 2): 3,
        5: 8,
        1.2: 6.0,
        True: {"hello": "another dict", 4: 3}
    }
    # ключ может быть тем же что и элемента set'a - всё кроме list, set, dict
    # значением в словаре может быть всё, что угодно. Даже другой словарь :)
    print(d, type(d))

    # функция выполняется в момент вызова. () - это вызов
    d['function']()

    moon = d["moon"]
    print(moon, d[True][4])
    print(d[5])
    d[5] = 13
    print(d[5])

    # индексирование словарей происходит так же, как в списках и кортежах, только индексы - это ключи
    # слайсы со словарём не работают

    # print(d["THIS IS NEW KEY"]) нельзя обращаться к ключам, которых еще нет в словаре
    d["THIS IS NEW KEY"] = "really?"
    print(d["THIS IS NEW KEY"])

    # как менять значения под ключами словаря
    # d["moon"] = d["moon"] + ", месяц"
    # d["moon"] = (d["moon"], "месяц")
    d["moon"] = [d["moon"], "месяц"]
    print(d['moon'])
    print(d)

    # проверяем есть ли хоть какие-то ключи в словаре
    if d:
        print(f'Словарь {d} не пустой')

    new_d = dict()
    if not new_d:
        print(f'Словарь {new_d} пустой')
    else:
        print(f'Словарь {new_d} не пустой')

    # проверяем есть ли известный нам ключ в том или ином словаре
    if 'moon' in d:
        print('Ключ moon есть в словаре d')

    if 'moon' not in new_d:
        print('Ключа moon нет в словаре new_d')

    print(len(d))
    # len работает на словарях и возвращает количество пар ключ-значение

    print(len(new_d))
    new_d['new_key'] = 'new_value'
    print(len(new_d))

    print(new_d.keys())
    print(list(d.keys()))
    for key in d:
    # for key in d.key(): эти две строчки одинаковые
        # если запустить цикл for (сделать итерацию) по словарю, то он будет возвращать ключи
        print(key, d[key])

    for value in d.values():
        print(value)
        # print(d[value]) это ошибка, связь ключ-значение работает только в одну сторону, а не в обе

    # самый удобный вариант прохода по словарю
    for key, value in d.items():
        print(key, value)
