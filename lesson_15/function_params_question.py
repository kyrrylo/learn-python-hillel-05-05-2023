from random import choices


def eat(self, random_foods):
    if self._hungry:
        for food in random_foods:
            if food in self.food:
                string_eat = f"Вы предложили {self.name} {random_foods}\n{self.name} кушает {food}"
                self._hungry = False
                return string_eat
        string_eat = f"Вы предложили {self.name} {random_foods}\n{self.name} не может есть {', '.join(random_foods)}"
        return string_eat


if __name__ == '__main__':
    foods = ["Рыба", "Молоко", "Каша", "Рис", "Тортик", "Мышь", "Тунец", "Консервы", "Сухой корм", "Вискас",
             "Курица", "Молоко"]
    # вход в функцию через рандом
    random_foods = choices(foods, k=6)
    eat(None, random_foods)
    # вход в функцию через захардкоженные значения
    eat(None, ['Консерва', 'Корм'])
    # вход в фунцию через инпут пользователя
    food = input('Чем кормить кошку? ')
    eat(None, [food])
    # вход в функцию через чтение текстового файла
    with open('cat_food.txt') as fh:
        food = fh.readlines()
        eat(None, [food])
