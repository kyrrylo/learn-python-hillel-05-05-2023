# ToDO сделать устойчивым конвертирование ввода пользователя в число
# \n - переход на новую строку

# пока
# while <conditional expression> == True:
    # тело цикла с отступом
print()
age = ''
while type(age) != int:
    age = input('Сколько вам полных лет?\n>')
    # попробовать
    # выполняется до первой ошибки. Если ошибка произошла, то весь последующий код,
    # включая строку с ошибкой не выполняется и мы переходим в блок except
    try:
        print('Это происходит до отлова ошибки')
        age = int(age)
        print('Это происходит после отлова ошибки')
    # обработка ошибки
    # срабатывает только если в блоке try была ошибка
    except Exception:
        print(f'Не удалось получить число из ввода: "{age}", повторите пожалуйста попытку')

name = input('Как вас зовут?')

# elif - else-if

# связующие

# and - и
# True and True = True
# True and False = False
# False and True = False
# False and False = False

# or - или
# True or True = True
# True or False = True
# False or True = True
# False or False = False

if age <= 0:
    print("Ты еще не родился!")
if age > 0 and age <= 6:
    print("Ты еще маленький")
if 6 < age <= 18:
    print("Ты ещё подросток")
"""if 6 < age < 18:
    print("Ты ещё подросток")"""
if age > 18 and age <= 60:
    print("Ты взрослый")
if age > 60 and age <= 90:
    print("Ты пожилой")
if age > 90:
    print("Ты долгожитель")


if age <= 0:
    print("Ты еще не родился!")
else:
    # этот elif проверяется только в том случае, когда содержимое if == False
    if age <= 6:
        print("Ты еще маленький")
    elif age <= 18:
        print("Ты ещё подросток")
    elif age <= 60:
        print("Ты взрослый")
    elif age <= 90:
        print("Ты пожилой")
    else:
        print("Ты долгожитель")
    print(f'Приятно познакомиться, {name}')


# cmd = input('Введите команду:')
# search
# sort
# view
# exit
