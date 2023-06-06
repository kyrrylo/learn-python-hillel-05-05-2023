test_strings = [
    'Я рад что ты пришел (нет) :( это было ужас... :)',
    'Я рад что ты пришел (нет) :( это было ужас... :',
    'аха(фывыф фывфыв) слово',
    'Hello (text) :) (hi) more text!',
    'Hello (text фыв) :) ( фывф hi) more text!'
]

for s in test_strings:
    new_words = list()
    to_add = True
    for word in s.split():
        opening_index = word.find('(')
        closing_index = word.rfind(')')
        # найдена открывающая скобка и мы сейчас в режиме добавлять всё
        if opening_index != -1 and to_add:
            # переходим в режим ничего не добавлять
            to_add = False
            # добавляем ту часть слова, которая до открывающей скобки (если такая часть слова есть)
            if word[:opening_index]:
                new_words.append(word[:opening_index])
            # если в этом слове есть еще и закрывающая скобка и она ПОСЛЕ открывающейся, то мы возвращаемся
            # в режим добавлять всё
            if closing_index > opening_index:
                to_add = True
        # найдена закрывающая скобка и мы сейчас в режиме не добавлять ничего
        elif closing_index != -1 and not to_add:
            # вернуться в режим добавлять всё
            to_add = True
            # добавляем ту часть слова, которая после закрывающей скобки (если такая часть слова есть)
            if word[closing_index + 1:]:
                new_words.append(word[closing_index + 1:])
        elif to_add:
            new_words.append(word)
    print(s, '->', ' '.join(new_words))
