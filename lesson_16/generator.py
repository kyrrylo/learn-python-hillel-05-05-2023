def regular_return_function(n: int):
    my_list = list()
    for i in range(n):
        my_list.append(i + 1)
    return my_list

# функции бывают трёх типов:
#   1. Есть return (возвращает значение)
#   2. Есть yield (генерирует значение)
#   3. Нету yield и return (ничего не возвращают)
#   4. Есть и yield и return (python по своей природной гибкости это позволяет, но на практике это не применяется)


# generator - это тип функций
# generator - это итеративный тип данных
def generator_function(n: int):
    print('Start of generator function')
    for i in range(n):
        # yield = добыча, урожай, элемент генерации
        yield i + 1
        # при повторном вызове генератора, функция работает НЕ сначала, а с момента где в предудыщий раз сработал yield
        print(f'Сгенерировано значение {i+1}')


if __name__ == '__main__':
    # список сразу загружает всё в память компьютера
    large_list = regular_return_function(1000000)
    large_generator = generator_function(1000000)
    print(f'List size: {large_list.__sizeof__()}')
    print(f'Generator size: {large_generator.__sizeof__()}')

    print(regular_return_function(10))

    # go through whole database
    current_generator = generator_function(10)
    for element in current_generator:
        print(element)
        print(f'Generator size: {current_generator.__sizeof__()}')
        # process database entry
