class Restaurant:

    """Создаем класс Ресторан."""
    def __init__(self, restaurant_name, cuisine_type):
        """Инициализирует атрибуты описания ресторана."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Метод, который выводит два атрибута"""
        print(f"Вас приветствует ресторан {self.restaurant_name}!")
        print(f"У нас представлена {self.cuisine_type} кухня!")

    def open_restaurant(self):
        """Метод который выводит сообщение о том, что ресторан открыт"""
        print(f"\nРесторан {self.restaurant_name} сейчас открыт!")


restaurant = Restaurant('4YOU', 'русская')
print(f"Ресторан: \n- {restaurant.restaurant_name}\n")
print(f"Кухня: \n- {restaurant.cuisine_type}\n")

restaurant.describe_restaurant()
restaurant.open_restaurant()