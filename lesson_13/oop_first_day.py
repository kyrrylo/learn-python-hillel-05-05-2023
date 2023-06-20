d = {
    "function1": lambda x: 5,
    "function2": None,
    "attribute1": 5,
    "attribute2:": "Ящерица"
}

# z = Dog() переменные класса можно создавать после объявления этого класса

class Dog:
    # тело класса
    name = "Тузик"
    # self - обязательный параметр методов класса (метод - это функция в классе), который должен быть первым
    def __init__(self):
        """ self - Это контекст класса, через него можно обратиться ко всему, что есть в классе
        self.bark()
        self.name
        self.__init__()
        """
        print('Создан объект класса Dog')

    def bark(self):
        print('Гав-гав')



class NoInitClass:
    def some_method(self):
        print('This is some method')


if __name__ == '__main__':
    print(Dog, type(Dog), type(int), type(float), type(str), type(bool), type(list), type(dict), type(set), type(tuple))
    # имя класса и две скобочки - это автоматический вызов метода __init__ (инициализация / initialization)
    d = Dog()
    x = Dog()
    y = Dog()
    z = Dog()
    print(d, x, y, z)
    print(type(d), type(x), type(y), type(z))
    print(d.name)
    d.bark()

    # класс - это "пользовательский" (кастомный, настраиваемый) тип данных
    # можно создавать переменные этого типа после объявления класса
    # созданные переменные класса называются объектами (object) или инстансами (instance) этого класса

    print(d.name, x.name, y.name, z.name)
    d.name = "Чижик"
    print(d.name, x.name, y.name, z.name)
    Dog.name = "Бобик"
    print(d.name, x.name, y.name, z.name)

    no_init = NoInitClass()
    print(no_init)