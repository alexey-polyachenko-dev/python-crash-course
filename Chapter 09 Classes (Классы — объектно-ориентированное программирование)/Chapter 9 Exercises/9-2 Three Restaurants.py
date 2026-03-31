class Restaurant:

    """Создаем класс Ресторан."""
    def __init__(self, restaurant_name, cuisine_type):
        """Инициализирует атрибуты описания ресторана."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Метод, который выводит два атрибута"""
        print(f"Вас приветствует ресторан '{self.restaurant_name}'!")
        print(f"У нас представлена {self.cuisine_type} кухня!\n")

    def open_restaurant(self):
        """Метод который выводит сообщение о том, что ресторан открыт"""
        print(f"\nРесторан {self.restaurant_name} сейчас открыт!")


restaurant_1 = Restaurant('4YOU', 'русская')
restaurant_2 = Restaurant('La France', 'французская')
restaurant_3 = Restaurant('Дядюшка Li', 'китайская')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()