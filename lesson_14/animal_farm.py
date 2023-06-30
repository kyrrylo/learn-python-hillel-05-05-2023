from animals import Dog, Hen, Cow
from random import choices, choice, randint

if __name__ == '__main__':
    animals = [
        Dog('Жучка', 3),
        Hen('Коко', 2),
        Cow('Милка', 5)
    ]

    available_food = ['сено', 'трава', "зерно", "пшено", "каша", "мясо", "кость", "тортик"]

    what_we_got = list()
    what_we_lost = list()
    for animal in animals:
        animal.say()
        """ то же самое, что и ниже
        for i in range(3):
            food = choice(available_food)
            animal.eat(food)
        """
        for food in choices(available_food, k=3):
            what_we_lost.append(food)
            animal.eat(food)
        if animal.hungry:
            print(f'{animal} голодает! Покормите его.')
        what_we_got.append(animal.treat(randint(0, 5)))
        print('=' * 20)

    print(f'Сегодня на ферме мы потратили: {", ".join(what_we_lost)} и получили {", ".join(what_we_got)}')
