from .person import Person


class Car:
    def __init__(self, name: str, fuel_tank_capacity: int, car_owner: Person):
        self.name = name
        self.__capacity = fuel_tank_capacity
        self.__fuel_level = fuel_tank_capacity
        # по умолчанию машина на 1 км будет тратить 0.1 литра топлива
        self.__fuel_consumption = 0.1

        self.owner = car_owner

    def __str__(self):
        return f'Машина {self.name}, владелец {self.owner.name}'

    @property
    def capacity(self):
        return self.__capacity

    @property
    def fuel_level(self):
        return self.__fuel_level

    @fuel_level.setter
    def fuel_level(self, x):
        """
        Устанавливает новый уровень топлива
        Новый уровень должен быть выше старого
        :param x: новый уровень топлива
        """
        if isinstance(x, float) or isinstance(x, int):
            if x > self.__fuel_level:
                self.__fuel_level = x
                if self.__fuel_level > self.__capacity:
                    self.__fuel_level = self.__capacity

    def add_fuel(self, fuel_amount):
        """
        Добавляет топливо в бак
        :param fuel_amount: сколько добавить
        """
        if isinstance(fuel_amount, float) or isinstance(fuel_amount, int):
            if fuel_amount > 0:
                self.__fuel_level += fuel_amount
                if self.__fuel_level > self.__capacity:
                    self.__fuel_level = self.__capacity

    def ride(self, km: int) -> bool:
        """
        Функция отвечает за обновление внутренних полей класса Car после поездки на указанное количество километров
        Если топлива не хватает на поездку, то поездка отменяется
        :param km: сколько км нужно проехать
        :return: True если поездка состоялась и False если не состоялась
        """
        fuel_required = self.__fuel_consumption * km
        # случай когда топлива хватает
        if fuel_required <= self.__fuel_level:
            self.__fuel_level -= fuel_required
            print(f'Машина {self.name} проезжает {km}км, в баке остаётся {self.__fuel_level}л топлива.')
            return True
        # случай когда топлива не поездку не хватит
        else:
            print(f'Машине {self.name} не хватит {self.__fuel_level}л топлива, чтобы проехать {km}км. '
                  f'Нужно заправиться перед поездкой!')
            return False
