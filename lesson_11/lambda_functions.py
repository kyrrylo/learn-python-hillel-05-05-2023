my_number_list = [2, 5, 4, 0, -5, -100, -3]
my_str_list = 'Today we look into lambda functions'.lower().split()

print('=' * 10, '\nОбычная сортировка')
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

print('=' * 10, '\nСортировка по ключу')

# key: Callable # когда параметр/аргумент функции должен быть сам функцией, пишут Callable (вызываемый)
def example_function():
    print('Example function is called')
    return 1


example_function()
x = example_function
print('X is assigned example function')
x()
example_function()


def abs_function(element):
    return abs(element)


# key принимает функцию, которая обязана предоставлять значение используемое в сортировке.
# Значение высчитывается с использованием самого элемента
# После сортировки используются изначальные значения элментов, а не те которые использовались для сортировки
print(sorted(my_number_list, key=abs_function))
print(sorted(my_number_list, key=abs))


def square_function(element):
    return pow(element, 2)


print(sorted(my_number_list, key=square_function))

d = {
    "Monitors": 3,
    "Keyboard": 4,
    "Headset": 6,
    "Laptop": 2
}


def dict_element_getter(element):
    print(element, type(element))
    # то что return-ит функция из key будет использовано для сортировки
    return element[1]


# Словарь можно создать "легко" из списка парных кортежей.
# Первый элемент кортежа станет ключом, второй - значением
sorted_dictionary = dict(sorted(d.items(), key=dict_element_getter))
print(sorted_dictionary, type(sorted_dictionary))

# lambda-функции это так называемые однострочные, простые, анонимные функции
# у них нет имени они не рассчитаны на повторные вызовы

# lambda <входные параметры через запятую>: <что функция возвращает>
# lambda element: element[1]
print('Lambda sorting')
sorted_dictionary = dict(sorted(d.items(), key=lambda element: element[1]))
print(sorted_dictionary, type(sorted_dictionary))

# lambda <входные параметры через запятую>: <что функция возвращает>
lambda_f = lambda x, y: x + y
print(lambda_f(3, 4))
print(lambda_f(11, 4))

# тернарное выражение (ternary expression/operator | one-line conditional expression)
# <возвращаемое True значение> if <условное выражение> else <возвращаемое False значение>
x = 10 if 5 > 15 else 11
print(x)

print('Условное выражение в одну строчку в lambda функции')
# лямбда функция принимает два параметра x, y
# возвращает произведение x и y если y != 0, в противном случае возвращает x
another_lambda_f = lambda x, y: x * y if y != 0 else x
print(another_lambda_f(5, 2))  # 10 потому что y != 0
print(another_lambda_f(5, 0))  # 5 потому что y == 0


def not_lambda_f(x, y):
    if y != 0:
        return x * y
    return x


print(not_lambda_f(5, 2))
print(not_lambda_f(5, 0))

print(max(my_number_list, key=lambda x: pow(x, 4)))

lambda_f_dict = {
    ""
}
