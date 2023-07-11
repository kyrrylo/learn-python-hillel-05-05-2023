x = list()
for element in range(10):
    x.append(element + 1)
print(type(x), x)

# list comprehension
# [<элемента списка> for <объявление переменной> in <по чему итерируемся>]
# [<однострочное тело цикла for> for <объявление переменной> in <по чему итерируемся>]
x = [element + 1 for element in range(10)]
print(type(x), x)

# Dict comprehension
x = dict()
for element in range(10):
    x[element + 1] = -(element + 1)
print(type(x), x)

# Dict comprehension
# {<ключ>: <значение> for <объявление переменной> in <по чему итерируемся>}
# {<однострочное тело цикла for> for <объявление переменной> in <по чему итерируемся>}
x = {element + 1: -(element + 1) for element in range(10)}
print(type(x), x)

# Set
x = set()
for element in range(10):
    x.add(element + 1)
print(type(x), x)

# set comprehension - то же самое что список, но скобочки фигурные
# {<элемента списка> for <объявление переменной> in <по чему итерируемся>}
# {<однострочное тело цикла for> for <объявление переменной> in <по чему итерируемся>}
x = {element + 1 for element in range(10)}
print(type(x), x)

# Generator
def generator():
    for element in range(10):
        yield element + 1

print(type(generator()), generator())
print(list(generator()))

# generator comprehension - то же самое что список, но скобочки круглые
# (<элемента списка> for <объявление переменной> in <по чему итерируемся>)
# (<однострочное тело цикла for> for <объявление переменной> in <по чему итерируемся>)
x = (element + 1 for element in range(10))
print(type(x), x)
print(list(x))