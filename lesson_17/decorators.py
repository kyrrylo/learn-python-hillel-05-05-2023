# decorator - это служебная функция, к которой есть строгие структурные требования
# если она составлена верно, то имя функции-декоратора можно писать над другими функциями через @ и тогда декоратор
# будет применем к функцию над которой написан

# требования к структуре функции-декоратора
# должен быть один входной параметр и сюда передана функция, к которой применяется декоратор
# в декораторе должна быть под-функция (функция внутри другой функции - уровень вложенности 2)
#   такую под-функцию нельзя вызвать за пределами функции-родителя
#   под-функция должна быть подобна функции, к которой применяется декоратор
#   и должна вызывать её внутри: result = decorated_function(*args, **kwargs)
#   под-функция должна возвращать то, что возвращает декорируемая функция: return result
# функция декоратора должна вернуть свою под-функцию: return wrapper
def my_decorator(decorated_function):
    # вывод: в начале работы программы декоратор выполняется частично и мы видим это в консоли
    print(type(decorated_function), decorated_function)
    print(5)
    def wrapper(*args, **kwargs):
        print('Before function')
        result = decorated_function(*args, **kwargs)
        print('After function')
        return result

    return wrapper


@my_decorator
def my_function(param1):
    print(f'this function received {param1}')


@my_decorator
def my_function2(param2: int):
    print(pow(param2, 2))
    return pow(param2, 3)


@my_decorator
def args_n_kwargs_function(*args, **kwargs):
    # * перед названием параметра означает что функция принимает любые параметры по порядку (через запятую)
    # в эту переменную: *args. Они будут представлены там элементами кортежа
    # ** перед названием параметра означате что функция принимате любые названные параметры
    # в эту переменную: **kwargs. Они будут представлены там элементами словаря
    print(type(args), args, len(args))
    print(type(kwargs), kwargs)

if __name__ == '__main__':
    print('first call')
    args_n_kwargs_function(5, 'Гватемала', 'Python', True, None, {1, 3, 9})
    print('second call')
    args_n_kwargs_function(param1=5, param2='Javascipt', param3= False, param4=[5, 6, 11, True])
    print('third call')
    args_n_kwargs_function(
        5, 'Гватемала', 'Python', True, None, {1, 3, 9},
        param1=5, param2='Javascipt', param3= False, param4=[5, 6, 11, True]
    )

    my_function(10)
    my_function2(20)