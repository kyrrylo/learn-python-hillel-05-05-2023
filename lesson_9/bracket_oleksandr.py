s = 'Я не знав куди йти (втім недивно), (text): тому пішов...'

what_we_seek = '('
new_s = ''
i = s.find(what_we_seek)  # находим первый индекс '(' в строке s и проверяем условие в цикле while i != -1

while i != -1:
    print(i)  # Для себя выводил индекс, чтобы придумать дельнейший ход задачи

    if what_we_seek == '(' and i != -1:
        what_we_seek = ')'
        new_s += s[:i]
        print(new_s)  # Выводил переменную на экран, для проверки

    elif what_we_seek == ')' and i != -1:
        what_we_seek = '('
        new_s += s[i + 1:]

    i = s.find(what_we_seek, i + 1)
print(new_s)