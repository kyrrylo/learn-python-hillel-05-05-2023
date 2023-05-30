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


x = 3
print('1', x)
this_apartment_voltage = 220
my_function(this_apartment_voltage)
my_function2(this_apartment_voltage)
my_function3(this_apartment_voltage)
print('2', x)

print('calling my function')
print(my_function(this_apartment_voltage))
