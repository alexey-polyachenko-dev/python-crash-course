class Restaurant:

    """Создаем класс Ресторан."""
    def __init__(self, restaurant_name, cuisine_type):
        """Инициализирует атрибуты описания ресторана."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Метод, который выводит два атрибута"""
        print(f"Вас приветствует ресторан {self.restaurant_name}!")
        print(f"У нас представлена {self.cuisine_type} кухня!")

    def open_restaurant(self):
        """Метод который выводит сообщение о том, что ресторан открыт"""
        print(f"\nРесторан {self.restaurant_name} сейчас открыт!")

    def set_number_served(self, visitor):
        """Метод, позволяющий задать количество обслуженных посетителей."""
        self.number_served = visitor

    def increment_number_serverd(self, add_visitor):
        """Метод, который увеличивает колличество обслуженных посетителей
        на заданную величину"""
        self.number_served += add_visitor

    def get_number_served(self):
        print(self.number_served)

class IceCreamStand(Restaurant):
    """Потомок класса Restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Инициализирует атрибуты класса-родителя.
        Затем инициализируем атрибуты, спецефические для киоска с мороженым."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['сливочное', 'шоколадное', 'с манго', 'с апельсином']

    def menu(self):
        """Выводит список сортов мороженого"""
        print("В наличии следующие сорта мороженого:")
        for flavor in self.flavors:
            print(f"- {flavor}")