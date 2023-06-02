import time

MY_CONSTANT_PI = 3.14


# namespace
# space - место name - имя
# именное пространство или зона видимости имени


def my_function2(voltage2):
    print('Inside function #1', x)
    # x = 5
    print('Inside function #2', x)


def my_function3(voltage2):
    print('Inside function #1', x)
    # x = 5
    print('Inside function #2', x)


def my_function(voltage):
    print('Inside function #1', x)
    # x = 5
    print('Inside function #2', x)


# Рекомендация: внутри и снаружи функций не использовать одинаковые имена переменных
# Чтобы не создавать конфликт интерпретации кода

# Код в Python можно поделить на две части:
# Внутри функций (выполняется только при вызове функции)
# Снаружи функций (выполняется при запуске файла)

# Весь код снаружи функций должен быть в одном месте и объединен в структуру __name__ == "__main__"
# if __name__ == '__main__': в одном файле должно быть только один раз
if __name__ == '__main__':
    x = 3

    t0 = time.time()
    print('1', x)
    this_apartment_voltage = 220
    my_function(this_apartment_voltage)
    my_function2(this_apartment_voltage)
    my_function3(this_apartment_voltage)
    print('2', x)

    print('calling my function')
    print(my_function(this_apartment_voltage))

# В .py файлах код должен присутствовать только в одном из 4 видов:
# 1. В начале файла import
# 2. В начале файла константы (переменная объявленная в верхнем регистре и которая не
#       изменяется за всю программу - её только читают и в неё не записывают)
# 3. Код внутри функций
# 4. Код под всеми функциями внутри if __name__ == '__main__':
# Весь остальной код является некорректный
