class Animal:
    def __init__(self, name: str, age: int, say_word: str, preferred_food: set):
        """
        Класс отвечает за симуляцию жизнедеятельности животного на ферме
        :param name: имя животного
        :param age: возраст животного
        :param say_word: какой "фразой" животное симулирует разговор
        :param preferred_food: рацион питания
        """

        # Incapsulation вносит уровни доступа
        # public - переменную можно смотреть и менять (read & write) снаружи и изнутри класса
        # _protected - переменную можно смотреть снаружи класса, а смотреть и менять только изнутри
        # __private - переменную можно менять и смотреть только изнутри класса
        self.animal_type = '???'
        self.name = name
        self.age = age
        self.say_word = say_word
        self.preferred_food = preferred_food
        self._hungry = True

        self._parameter_cant_be_less_than_100 = 150
        self._protected_animal_field = 10
        self.__private_animal_field = 20

    @property
    def parameter_z(self):
        return self._parameter_cant_be_less_than_100

    @parameter_z.setter
    def parameter_z(self, x):
        if type(x) == int or type(x) == float:
            if x >= 100:
                self._parameter_cant_be_less_than_100 = x

    # это - getter
    @property
    def hungry(self):
        return self._hungry

    def get_hungry(self):
        return self._hungry

    def set_hungry(self, x):
        pass

    # d.set_hungry(True)
    # d.set_parameter_z(1000)

    @hungry.setter
    def hungry(self, x):
        print(f'Вызвана функция hungry.setter, сюда передано значение {x}')
        if isinstance(x, bool):  # isinstance - то же самое, что type(x) == bool, но корректнее
            self._hungry = x

    def __str__(self):
        return f'{self.animal_type} {self.name}. Голод: {self._hungry}'

    def say(self):
        """
        Животное произносит заготовленные "фразы" для привлечения внимания в чате :)
        """
        print(f'{self} говорит: {self.say_word}')

    def eat(self, food: str):
        """
        Метод отвечает за симуляцию еды у животного на ферме
        Если предложенная еда есть в preferred_food, то животное наестся и self.hungry = False
        иначе животное не покушает
        :param food: что кушаем
        """
        if not self._hungry:
            return
        if food in self.preferred_food:
            print(f'{self} кушает {food}')
            self._hungry = False
        else:
            print(f'{self} такое не ест: {food}')
            self.say()

    def treat(self, hours: int):
        """
        Метод ухаживания за животным
        :param hours: сколько часов мы проводим с животным
        :return: что получаем взамен
        """
        raise NotImplementedError


class Dog(Animal):
    def __init__(
            self,
            name: str,
            age: int,
            say_word='Гав-гав!'
    ):
        """
        Класс отвечает за симуляцию животного собака
        """
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={'каша', 'мясо', 'кость'}
        )
        self.animal_type = 'Собака'

        self._protected_dog_field = -10
        self.__private_dog_field = -20

        self.__private_say_function()

    def __private_say_function(self):
        print('Protected field:', self._protected_dog_field)
        print('Private field:', self.__private_dog_field)
        print('Protected super field:', self._protected_animal_field)
        print('Private super field:', self._Animal__private_animal_field)

    def treat(self, hours: int) -> str:
        """
        Ухаживая за собакой должное количество времени, мы получаем хорошее настроение
        :param hours: сколько часов ухаживаем
        :return: ничего или хорошее настроение
        """
        if hours > 2:
            print(f'Вы гуляете с {self} {hours} часов, у вас повышается настроение, а собака нагуляла аппетит.')
            self._hungry = True
            return 'Хорошее настроение'
        print(f'Вы гуляете с {self} {hours} часов.')
        return ''


if __name__ == '__main__':
    d = Dog('Бобик', 4)
    # менять protected поля снаружи пайтон хоть и позволяет, но делать это нежелательно
    # d._hungry = 10
    # print(d._hungry)
    print(d)

    # getter - получатель, функция-читатель reader
    # setter - установщик, функция-писатель writer
    # функции для изменения защищённых (протектед и приватных) полей классов
    # эти функции контроллируют "санкционное" пользование этими полями

    print('Protected self field', d._protected_dog_field)
    # print(d.__private_dog_field) снаружи класса недоступно приватное поле
    # d.__private_say_function() функции тоже могут быть приватными
    print('Protected super field', d._protected_animal_field)
    # print('Private super field', d.__private_animal_field)

    for potential_value in [10, 'Голодная', False, -1, None, (123, 144), {'adsa': 5}, {3, 4}, [2, 'asd', 4]]:
        d.hungry = potential_value
        print(d)
        print(d.hungry)

    for potential_value in [10, 200, 'Голодная', False, -1, 90, 400, None, (123, 144), {'adsa': 5}, {3, 4}, [2, 'asd', 4]]:
        d.parameter_z = potential_value
        print(d.parameter_z)

    a = Animal('???', 20, 'AAA', {'???', '??'})

    print('Является ли ??? собакой: ', type(a) == Dog)
    print('Является ли ??? животным: ', type(a) == Animal)

    print('Является ли Бобик собакой: ', type(d) == Dog)
    print('Является ли Бобик животным: ', type(d) == Animal)

    # isinstance(a, b) является ли а представителем класса b

    print('Является ли ??? собакой (isinstance): ', isinstance(a, Dog))
    print('Является ли ??? животным (isinstance): ', isinstance(a, Animal))

    print('Является ли Бобик собакой (isinstance): ', isinstance(d, Dog))
    print('Является ли Бобик животным (isinstance): ', isinstance(d, Animal))
