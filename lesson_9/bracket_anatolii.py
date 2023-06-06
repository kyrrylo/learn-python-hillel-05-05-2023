# Я не знав куди йти) (втім недивно)), (text): тому пішов...

text = input('''Enter your text here: \n >''')  # Ввод пользователя
for i in range(len(text)):      # Цикл перебора символов в строке
    if '(' in text:     # Условие если скобка найдена
        opening = True         # Флаг на открытую скобку
        start = text.index('(')     # Узнаем индекс открытой скобки
    else:
        opening = False     # Условие если скобок нет
    if ')' in text:     # Условие если скобка закрывается
        close = True    # Флаг на закрытую скобку
        stop = text.index(')')      # идекс закрывающей скобки
        """
        while stop < start:
            stop = text.find(')', stop + 1)
            if stop == -1:
                close = False
                break
        """
    if opening == close:    # Если оба флага True значит делаем удаление через срез
        text = text[:start] + text[stop + 1:]       # Условие среза
        continue    # продолжаем до тех пор пока не закончится рейнж цикла что бі найти все скобки
print(f'Well Done! \n {text}')     # Вывод пользователю