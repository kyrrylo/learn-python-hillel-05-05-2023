# list == список

x = list()

print(type(x))
print(x)

x = [3, 4, 5]
print(type(x))
print(x)

x = [3, 3.5, 'I am string', False, [5, 'Another list', True]]
print(type(x))
print(x)

# list - Это такой тип данных, который может содержать в себе от 0 до N других переменных
# Они всегда будут хранится по порядку
i = 0
print(f'{i}-ый элемент: {x[i]}')
print(x[-1][1])

# для каждого элемента <новая-переменная-итератор> из <по чему итерируемся>:
#     тело for
print('BY ELEMENT')
for element in x:
    print(element)

print('BY ITERATOR')
for i in range(5):
    print(x[i])
