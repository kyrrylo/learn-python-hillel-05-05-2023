def max_min_sort_on_iterative_data():
    my_number_list = [4, 2, -100, 5.5, 32, 65, 22, 3.4, 2.5, -3.9]
    my_str_list = "My name is Kyrylo. I write code in programming language." \
                  " I am machine learning Engineer and Product Owner.".lower().split()

    print('len', len(my_number_list))
    print('len', len(my_str_list))

    print('sum', sum(my_number_list[:3]))
    print('sum', sum(my_number_list))

    # print(sum(my_str_list))  # не работает на строки
    """ # работает примерно так же, как ДЗ 4
    my_sum = 0
    while True:
        x = int(input('User number: '))
        my_sum += x
    """

    print('max', max(my_number_list))
    print('min', min(my_number_list))

    print('max', max(my_str_list))
    # проверяет от первой и далее каждую следующую букву.
    # чем ближе эта буква к началу алфавита, тем меньше получается значение (ближе к min)
    # у коротких слов меньше букв и выше шанс оказаться впереди
    # большие буквы идут перед маленькими буквами
    print('min', min(my_str_list))

    # сортировка по возрастанию (ascending)
    print(sorted(my_number_list))
    # сортировка по убыванию (descending)
    print(sorted(my_number_list, reverse=True))

    # сортировка по возрастанию (ascending)
    print(sorted(my_str_list))
    # сортировка по убыванию (descending)
    print(sorted(my_str_list, reverse=True))

    my_number_tuple = tuple(my_number_list)

    # .method()
    # function()

    sorted_tuple = sorted(my_number_tuple)
    print(type(sorted_tuple), sorted_tuple)

    my_number_set = set(my_number_list)
    sorted_set = sorted(my_number_set)
    print(type(sorted_set), sorted_set)


    print(my_number_list)
    # сортирует на месте, перетирая предыдущее состояние списка. Не возвращает ничего
    # в остальном - полностью идентичен методу sorted
    print(my_number_list.sort())
    print(my_number_list)
    # как красиво сортировать dictionary - с помощью lambda функций (чуть позже вернёмся)
    # по умолчанию сортируются только ключами и это мало-применимо


def pop_remove_from_list():
    my_number_list = [4, 2, -100, 5.5, 32, 65, -100, 22, 3.4, 2.5, -3.9]
    new_list = list()
    for x in my_number_list:
        if x > 0:
            new_list.append(x)
    print(new_list)

    # remove убирает 1 элемент списка по значению. Чтобы убрать все с таким значением,
    # нужно запускать несколько раз
    # в функцию заложен поиск по списку, но т.к. это дорогостоящая операция, то функция непопулярна
    x = my_number_list.remove(-100)  # функция ничего не возвращает
    print(x)
    print(my_number_list)

    # pop по индексу элемента списка удаляет его из списка и возвращает значение удалённого элемента
    # "вынуть"
    # pop используется в разных алгоритмах весьма часто

    # my_number_list.pop(300)  # можно вытаскивать только то, что есть в списке

    my_number_list.append([343, 32, 55, 32])
    my_number_list.append(True)
    my_number_list.append('The weather is beautiful')
    my_number_list.append({'z', 'x', 'y', 5})
    while my_number_list:  # пока список не пустой
        x = my_number_list.pop(-1)  # вытяни его первый элемент
        if type(x) == list:
            while x:
                print(x.pop(-1))
        print(x)

    print(my_number_list)


if __name__ == '__main__':
    print('Max/min/')
    max_min_sort_on_iterative_data()
    print('Pop/remove')
    pop_remove_from_list()
