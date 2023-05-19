# list == список

the_one_and_only_list = list()

print(type(the_one_and_only_list))
print(the_one_and_only_list)

the_one_and_only_list = [3, 4, 5]
print(type(the_one_and_only_list))
print(the_one_and_only_list)

the_one_and_only_list = [3, 3.5, 'I am string', 3, False, [5, 'Another list', True]]
print(type(the_one_and_only_list))
print(the_one_and_only_list)

print('LENGTH OF LIST') # длина списка
print(len(the_one_and_only_list))
the_one_and_only_list = [6, 3, 3.5, 'I am string', 3, False, 3 < 5, [5, 'Another list', True]]
print(len(the_one_and_only_list))

# list - Это такой тип данных, который может содержать в себе от 0 до N других переменных
# Они всегда будут хранится по порядку
i = 0
print(f'{i}-ый элемент: {the_one_and_only_list[i]}')
print(the_one_and_only_list[-1][1])

# для каждого элемента <новая-переменная-итератор> из <по чему итерируемся>:
#     тело for
print('BY ELEMENT')
for element in the_one_and_only_list:
    print(element)

print('BY ELEMENT ENUMERATED')
for i, element in enumerate(the_one_and_only_list):
    print(i, element, type(element))

print('BY ITERATOR')
for i in range(len(the_one_and_only_list)):
    print(i, the_one_and_only_list[i])
    if i == 3:
        break

print('SLICE')
# [<откуда, включительно>:<докуда, исключительно>]
print(the_one_and_only_list[1:3])
# [<откуда, включительно>:<докуда, исключительно>:<шаг>]
print(the_one_and_only_list[::2])  # все чётные
print(the_one_and_only_list[1::2])  # все нечётные
print(the_one_and_only_list[::-2])  # все чётные с конца
print(the_one_and_only_list[-2::-2])  # все нечётные с конца