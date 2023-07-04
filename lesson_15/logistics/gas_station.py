from .car import Car


class GasStation:
    def __init__(self, name: str, price_per_liter: float):
        self.name = name
        self.__price = price_per_liter

        self.my_car = None

    def refuel(self, car: Car, liters: int = None) -> float:
        """
        Метод отвечает за заправку машины Car на указанное количество liters
        Возвращает цену заправки
        :param car: машина, которую нужно заправить
        :param liters: количество литров топлива, если None, то до полного бака
        :return: цена self.__price * liters
        """
        # self.my_car = car если эту строку раскомментировать, то это будет агрегация, а не композиция

        # если передано None, то указываем максимально возможное значение для этой машины
        if isinstance(liters, type(None)):  # type(liters) == None
            liters = car.capacity

        # фиксируем сколько было топлива до заправки
        prev_fuel_level = car.fuel_level
        # заправляем
        # car.fuel_level = car.fuel_level + liters
        car.add_fuel(liters)  # альтернативный способ заправки
        # фиксируем на сколько количество топлива поднялось
        real_liters = car.fuel_level - prev_fuel_level
        # высчитываем цену
        price = real_liters * self.__price
        print(f'{car.name} заправляется у {self.name} на {real_liters}л и это стоит: {price:.2f} UAH')
        return price
