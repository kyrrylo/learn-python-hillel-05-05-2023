from logistics import Car, GasStation, Person

if __name__ == '__main__':
    # класс Car содержит в одном из своих полей (owner) объект класса Person
    # это агрегация - полями одного класса являются объекты другого класса
    c = Car('Range Rover', 80, Person('John Smith'))

    print(f'Создаём {c}')
    # print(c.capacity) в классе есть property capacity, следовательно его можно прочитать
    # c.capacity = 20  однако нету setter'a на это proprty и записать его нельзя - такие права доступа

    wog = GasStation('WOG', 52)
    okko = GasStation('OKKO', 50)
    # сколько потрачено денег на топливо
    price = 0

    # поездка на машине
    # за хлебом
    c.ride(10)
    # в соседний город
    c.ride(300)
    # заправка

    # класс GasStation получает в свой метод объект класса Car
    # это композиция - классы взаимодействуют между собой
    # выходит что класс GasStation не может применить своё поведение refuel без объекта класса Car
    price += okko.refuel(c)
    # в соседнюю область
    c.ride(600)
    price += wog.refuel(c, 10)
    c.ride(20)
    price += okko.refuel(c, 30)
    c.ride(600)

    print(f'На топливо было потрачено: {price:.2f} UAH')