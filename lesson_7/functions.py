# def <имя функции>(<параметр функции 1>, <параметр функции 2>, ...):
def read_user_number(user_prompt: str, lower_bound: int = 0, upper_bound: int = 9999999):
    """
    Отвечает за считывание у пользователя строки и конвертации её в число
    Считывание происходит до тех пор, пока введённая строка не удовлетворит все условия
    :param user_prompt: комментарий для контекста пользователю
    :param lower_bound: нижнее допустимое значение
    :param upper_bound: верхнее допустимое значение
    :return: считанное у пользователя число в рамках допустимых значений
    """
    # тело функции на отступе
    while True:
        number = input(f'{user_prompt}\n>')
        try:
            number = float(number)
            if lower_bound < number < upper_bound:
                # return - выход из функции с возвращением некоего значения
                return number
                # return  # return без ничего возвращает None
            else:
                print(f'Введите число в таких рамках: от {lower_bound} до {upper_bound}')
        except Exception:
            print(f'Не удалось получить число из ввода: "{number}", повторите пожалуйста попытку')


z = 5
print(type(read_user_number), read_user_number)
a = read_user_number('Введите сторону треугольника a=')
fuel_liter_price = read_user_number('Введите цену за 1л топлива:')
age = read_user_number('Сколько вам полных лет?', upper_bound=150)
air_temperature = read_user_number('Какая температура воздуха?', lower_bound=-99999999, upper_bound=99999999)

print(a, fuel_liter_price, age, air_temperature)
