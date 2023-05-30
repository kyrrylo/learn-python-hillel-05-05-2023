fruits = ['apple', 'pineapple', 'pear', 'apricot']

# конкатенация (склеивание) списков
fruits = fruits + ['watermelon']
# fruits = fruits + 'watermelon' # склеиваются только списки со списками
fruits = ['banana'] + fruits

fruits.append('granat')
# append - добавить в конец списка элемент

fruits.insert(0, 'mango')
fruits.insert(len(fruits) // 2, 'coconut')
fruits.insert(len(fruits), 'kiwi')

for fruit in fruits:
    if len(fruit) > 6:
        print(fruit[:6])
    else:
        print(fruit)


# 'banana' + ['orange']

plants = [['banana', 'mango'], ['cucumber', 'cabbage', 'carrot', 'eggplant']]
plants[0].append('watermelon')
plants[0].insert(2, 'pear')
plants[0] = plants[0] + ['orange']
plants[0] = ['kiwi'] + plants[0]
print(plants)

p = [1, 2, 3, 4, 5, 6]
p2 = list()
for element in p:
    # p.append(8)
    p2.append(element ** 2)
    print(p2)

print(p)
print(p2)

s = 'My name is Kyrylo and I study Python and it is good. The weather is good.'
i = s.find('y')
print(i)
print(s.find('y', i + 1))
# Вывести все индексы буквы 'y'

print('Индексы через while')
# достоинство: может искать слова
# недостатки: сложнее понять как грамотно построить
what_we_seek = '('
i = s.find(what_we_seek)
new_s = ''
while i != -1:  # ищем до тех пор, пока find что-то находит. Если не найдёт - вернёт -1 и мы выйдем из цикла
    print(i)
    i = s.find(what_we_seek, i + 1)
    if what_we_seek == '(' and i != -1:
        what_we_seek = ')'
    elif what_we_seek == ')' and i != -1:
        what_we_seek = '('

new_s = s[:11] + s[50:]  # слайсы гораздо быстрее и эффективнее чем replace
s.replace('Kyrylo and I study Python and it is good', '')


print('Индексы через for')
# достоинство: легко находит буквы
# недостатки: слов находить сложно
for i, letter in enumerate(s):
    if letter == 'y':
         print(i)

# как работает enumerate и почему в for мы указываем два значения через запятую

for t in enumerate(s):
    print(type(t), t)
    i, letter = t
    print(i, letter)
