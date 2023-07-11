from time import time, sleep


def all_to_str(decorated_function):
    """
    Декоратор, который превращает все входные параметры в тип строка
    """
    def wrapper(*args, **kwargs):
        new_args = [str(arg) for arg in args]
        """ list comprehension
        new_args = list()
        for arg in args:
            new_args.append(str(arg))
        """
        new_kwargs = {key: str(value) for key, value in kwargs}
        """ dict comprehension
        new_kwargs = dict()
        for key, value in kwargs:
            new_kwargs[key] = str(value)
        """
        return decorated_function(*new_args, **new_kwargs)
    return wrapper


def execution_time(decorated_function):
    """
    Декоратор, который считает время выполнения функции и выводит это на экран
    """
    def wrapper(*args, **kwargs):
        t0 = time()
        result = decorated_function(*args, **kwargs)
        result_time = time() - t0
        print(f'Функция {decorated_function.__name__}'
              f' с параметрами args={args}, kwargs={kwargs} выполнялась '
              f'{result_time:.2f}s')
        return result
    return wrapper


@all_to_str
@execution_time
def sum_of_two(a: int, b: int):
    print(type(a), type(b))
    sleep(2)
    return a + b


if __name__ == '__main__':
    print(sum_of_two(10, 15))
