class Car:
    def __init__(self, fuel_quantity: (int, float), fuel_consumption: (int, float)):
        """
        Создание базового класса "Автомобиль"
        :param fuel_quantity: объем топлива в баке автомобиля
        :param fuel_consumption: расход топлива (л) на 1 км
        """
        self._fuel_quantity = None  # protected: не изменяется при выключенном двигателе
        self._init_fuel_quantity(fuel_quantity)
        self._fuel_consumption = None  # protected: константа для конкретного автомобиля
        self._init_fuel_consumption(fuel_consumption)

    def __str__(self) -> str:
        return f"Автомобиль: объем топлива {self.fuel_quantity} (л), расход топлива {self.fuel_consumption} (л/км)."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(fuel_quantity={self.fuel_quantity},fuel_consumption={self.fuel_consumption})"

    def _init_fuel_quantity(self, fuel_quantity: (int, float)) -> None:
        """
        Инициализация атрибута _fuel_quantity:
        Protected: используется только при инициализации экземпляра класса
        :param fuel_quantity: текущий объем топлива в баке
        """
        if not isinstance(fuel_quantity, (int, float)):
            raise TypeError('Объем топлива должен быть типа int или float')
        if fuel_quantity < 0:
            raise ValueError('Объем топлива должен быть не меньше 0')
        self._fuel_quantity = fuel_quantity

    def _init_fuel_consumption(self, fuel_consumption: (int, float)) -> None:
        """
        Инициализация атрибута _fuel_consumption:
        Protected: используется только при инициализации экземпляра класса
        :param fuel_consumption: расход топлива (л) на 1 км
        """
        if not isinstance(fuel_consumption, (int, float)):
            raise TypeError('Расход топлива должнен быть типа int или float')
        if fuel_consumption <= 0:
            raise ValueError('Расход топлива должнен быть больше 0')
        self._fuel_consumption = fuel_consumption

    @property
    def fuel_quantity(self) -> (int, float):
        """
        Используем getter для атрибута _fuel_quantity (не setter: protected атрибут)
        """
        return self._fuel_quantity

    @property
    def fuel_consumption(self) -> (int, float):
        """
        Используем getter для атрибута _fuel_consumption (не setter: protected атрибут)
        """
        return self._fuel_consumption

    def fill_fuel(self, added_fuel: (int, float)) -> None:
        """
        Заправить машину - увеличить объем топлива в баке
        :param added_fuel: объем добавляемого топлива
        """
        if not isinstance(added_fuel, (int, float)):
            raise TypeError('Объем добавляемого топлива должен быть типа int или float')
        if added_fuel < 0:
            raise ValueError('Объем добавляемого топлива должен быть не меньше 0')
        self._fuel_quantity += added_fuel

    def spent_fuel(self, route_length: (int, float)) -> None:
        """
        Определить объем потраченного топлива во время поездки
        :param route_length: длина маршрута
        """
        if not isinstance(route_length, (int, float)):
            raise TypeError('Длина маршрута должна быть типа int или float')
        if route_length < 0:
            raise ValueError('Длина маршрута должна быть не меньше 0')
        ...


class PassengerCar(Car):
    def __init__(self, fuel_quantity: (int, float), fuel_consumption: (int, float), quantity_seats: int):
        """
        Создание дочернего класса "Легковой автомобиль", унаследован от класса "Автомобиль"
        :param fuel_quantity: объем топлива в баке автомобиля
        :param fuel_consumption: расход топлива (л) на 1 км
        :param quantity_seats: количество пассажиромест в легковом автомобиле
        """
        super().__init__(fuel_quantity, fuel_consumption)
        self._quantity_seats = None  # protected: константа для конкретного автомобиля
        self._init_quantity_seats(quantity_seats)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(oil_amount={self.fuel_quantity},oil_consumption={self.fuel_consumption}," \
               f"seats={self._quantity_seats})"

    def _init_quantity_seats(self, quantity_seats: int) -> None:
        """
        Инициализация атрибута _quantity_seats - количество пассажиромест в легковом автомобиле
        Protected: используется только при инициализации экземпляра класса
        :param quantity_seats: количество мест в автомобиле
        """
        if not isinstance(quantity_seats, int):
            raise TypeError('Количество пассажиромест в легковом автомобиле должно быть типа int')
        if quantity_seats <= 0:
            raise ValueError('Количество пассажиромест в  легковом автомобиле должно быть больше 0')
        self._quantity_seats = quantity_seats

    @property
    def seats(self) -> int:
        """
        Используем getter для атрибута _quantity_seats (не setter: protected атрибут)
        """
        return self._quantity_seats

    def spent_fuel(self, route_length: (int, float)) -> None:
        """
        Определить объем потраченного топлива во время поездки
        Перегрузка метода базового класса ввиду того, чт едем на пассажирском автомобиле
        :param route_length: длина маршрута
        """
        if not isinstance(route_length, (int, float)):
            raise TypeError('Длина маршрута должна быть типа int или float')
        if route_length < 0:
            raise ValueError('Длина маршрута должна быть не меньше 0')
        ...
