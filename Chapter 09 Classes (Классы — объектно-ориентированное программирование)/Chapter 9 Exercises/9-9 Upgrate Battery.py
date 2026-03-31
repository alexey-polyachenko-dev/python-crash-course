class Car:
    """Простая модель автомобиля."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 20

    def get_descriptive_name(self):
        """Возвращает отформатированное описание."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Выводит данные о пробеге машины в милях."""
        print(f"This car has {self.odometer_reading} miles on it.")

    """Изменение атрибута с спомощью метода."""
    def update_odometer(self, mileage):

        """Устанавливает заданное значение на одометре.
        При попытке обратной подкрутки изменение отклоняется."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Увеличивает значение одометра с заданным приращением."""
        self.odometer_reading += miles

class Battery:
    """Простая модель батареи электромобиля."""
    def __init__(self, battery_size=40):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Выводит данные о приблизительном запасе хода для аккумулятора."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Проверяем размер аккумулятора и устанавливаем мощность равной 65,
        если она имеет другое значение"""
        if self.battery_size != 65:
            self.battery_size = 65
            print("\nUpgraded the battery to 65 kWh.")

class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя.
        Затем инициализируем атрибуты, спецефические для электромобиля."""
        super().__init__(make, model, year)
        self.battery = Battery()

my_leaf = ElectricCar('nissan', 'leaf', 2024)
my_leaf.battery.get_range()

my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()
