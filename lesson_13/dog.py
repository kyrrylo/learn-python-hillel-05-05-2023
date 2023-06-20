from random import choices, randint
# Класс - это не просто набор функций
# У класса обязан быть контекст в виде переменных
# Эти переменные отличают объекты класса друг от друга и делают их разными
# Переменные внутри класса называются свойствами, полями или атрибутами
# Свойства/поля/атрибуты класса задаются внутри метода __init__ через контекст объекта класса self:
# self.attribute_name = 5
# self.attribute_name_2 = 'This is a string'
# Если не удаётся придумать подходящее значение для поля класса, то можно объявить его None:
# self.unknown_attribute = None

# имена классов пишутся в CamelCase регистре
class Dog:
    # тело класса
    # self - обязательный параметр методов класса (метод - это функция в классе), который должен быть первым
    def __init__(self, name: str, age: int, breed: str, preferred_food: set):
        """
        Класс собака
        :param name: имя
        :param age: возраст
        :param breed: порода
        :param preferred_food: предпочитаемая еда
        """
        print('Создан объект класса Dog')
        self.name = name
        self.age = age
        self.breed = breed
        self.preferred_food = preferred_food

        # голодная ли собака
        self.hungry = True
        # сколько часов гуляла
        self.hours_outdoors = 0

    def __str__(self):
        starting_str = f"{self.breed} {self.name}, {self.age} "
        if self.age == 1:
            starting_str += "год"
        elif 2 <= self.age <= 4:
            starting_str += "года"
        else:
            starting_str += "лет"
        starting_str += f", часов гулял: {self.hours_outdoors}, голоден: {self.hungry}"
        return starting_str

    def bark(self, count: int):
        if count > 0:
            barking_str = '-'.join(["гав"] * count).capitalize()
            print(f"{self.name} гавкает: {barking_str}!")

    def eat(self, food: str):
        if self.hungry:
            if food in self.preferred_food:
                print(f"{self.name} кушает {food}")
                self.hungry = False
            else:
                self.bark(randint(1, 5))
                print(f"{self.name} такое не ест: {food}")
        else:
            print(f"{self.name} не голоден")


if __name__ == '__main__':
    # Как передавать значения в класс и делать объекты разными
    d = Dog('Бублик', 2, "мопс", {'каша'})
    # d = Dog.__init__('Бублик') # то же самое, что выше
    x = Dog('Чижик', 4, "дворняга", {'мясо', 'хлеб'})
    y = Dog('Бобик', 3, "канекорса", {'рыба', 'мясо', 'каша'})
    z = Dog('Тобик', 5, "овчарка", {'мясо', 'борщ', 'сало'})
    dogs = [d, x, y, z]
    """
    dogs = [
        Dog('Бублик', 2, "мопс", {'каша'}),
        Dog('Чижик', 4, "дворняга", {'мясо', 'хлеб'}),
        Dog('Бобик', 3, "канекорса", {'рыба', 'мясо', 'каша'}),
        Dog('Тобик', 5, "овчарка", {'мясо', 'борщ', 'сало'})
    ]"""
    print(d.name, x.name, y.name, z.name)
    print(d)
    print(x)
    print(y)
    print(z)

    potential_food = ['каша', 'хлеб', 'рыба', 'борщ', 'сало', 'торт', 'яблоко']
    for dog in dogs:
        print(f'Кормим {dog.name}')
        for random_food in choices(potential_food, k=3):
            dog.eat(random_food)
        print(dog)
