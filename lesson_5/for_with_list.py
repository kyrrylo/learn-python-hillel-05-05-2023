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

s = 'My name is Kyrylo and I study Python'
i = s.find('y')
print(i)
print(s.find('y', i + 1))
# Вывести все индексы буквы 'y'
