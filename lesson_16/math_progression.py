import math
from time import time


def generate_geom_progression(a: float, q: float, n: int):
    """
    :param a: С какого числа начинается прогрессия
    :param q: На какое число умножается каждый следующий элемент прогрессии
    :param n: Сколько чисел прогрессии нужно сгенерировать
    """
    yield a
    for i in range(n):
        a = a * q
        yield a


def batchify_geom_progression(a: float, q: float, n: int, batch_size: int = 100):
    """
    :param a: С какого числа начинается прогрессия
    :param q: На какое число умножается каждый следующий элемент прогрессии
    :param n: Сколько чисел прогрессии нужно сгенерировать
    :param batch_size: Какого размера батчи возвращать
    """
    batch = list()
    batch.append(a)
    for i in range(n):
        # yielding batches
        if len(batch) == batch_size:
            yield batch
            batch = list()
        # moving forward
        a = a * q
        batch.append(a)
    # yielding left-over
    if batch:
        yield batch


def geom_progression(a: float, q: float, n: int) -> list:
    """
    :param a: С какого числа начинается прогрессия
    :param q: На какое число умножается каждый следующий элемент прогрессии
    :param n: Сколько чисел прогрессии нужно вернуть
    :return: список чисел геометрической прогрессии длиной n
    """
    geom_p = list()
    geom_p.append(a)
    for i in range(n):
        a = a * q
        geom_p.append(a)
    return geom_p


if __name__ == '__main__':
    first_value = 13.5
    multiplier = math.e
    geom_count = 100000000
    to_print = False

    t0 = time()
    geom_list = geom_progression(first_value, multiplier, geom_count)
    print(f'Geometrical progression LIST: {geom_list.__sizeof__()}')
    for element in geom_list:
        if to_print:
            print(element, end=' ')
    print(f'\nTime taken: {time() - t0:.2f}s')

    print('\n', '=' * 10, sep='')

    t0 = time()
    geom_gen = generate_geom_progression(first_value, multiplier, geom_count)
    print(f'Geometrical progression GENERATOR: {geom_gen.__sizeof__()}')
    for element in geom_gen:
        if to_print:
            print(element, end=' ')
    print(f'\nTime taken: {time() - t0:.2f}s')

    print('\n', '=' * 10, sep='')

    # Серединный вариант. Самый медленный на таких данных, потому что нужно создавать на ходу списки (выделять память динамически)
    # Когда данные уже есть и от них надо "отрезать" куски (н-р чтение файла или базы данных), то батчи наоборот выигрышны
    t0 = time()
    geom_batch_gen = batchify_geom_progression(first_value, multiplier, geom_count, 100)
    print(f'Geometrical progression BATCH GENERATOR: {geom_gen.__sizeof__()}')
    for batch in geom_batch_gen:
        for element in batch:
            if to_print:
                print(element, end=' ')
    print(f'\nTime taken: {time() - t0:.2f}s')