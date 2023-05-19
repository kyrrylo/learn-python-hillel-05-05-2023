"""
while <условное выражение>( == True):
    тело цикла
"""
EXIT_COMMAND = 'exit'

# Итерация цикла - полная отработка тела цикла
# Например смена дней недели. Понедельник-Вторник-...Воскресенье - это одна итерация. Следующая итерация - с Понедельника
while True:
    x = input('1. Where are you from (type `exit` to leave)? ')
    # if 'exit' == x.lower(): # то же самое
    print("2. Второй вывод в цикле")
    if 'exit' != x.lower():
        print('3. Вы не вышли')
    else:
        print('3. About to exit')
        # команда выхода из цикла
        # позволяет выйти в месте где написано
        # условие в while позволяет выйти только между и итерациями
        break
        print('3. Already exited')
    print("4. Последний вывод в теле цикла")


print('Outside break-while!')

while True:
    x = input('Are you studying or working (type `exit` to leave)? ')
    # if 'exit' == x.lower(): # то же самое
    if 'exit' == x.lower():
        print('About to exit')
        # команда выхода из программы
        exit()
        # quit() то же, что и exit()
        print('Already exited')
    else:
        print('Вы не вышли')

print('Outside exit-while!')
