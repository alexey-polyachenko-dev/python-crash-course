class User:
    """Создаем класс User."""

    def __init__(self, first_name, last_name, age, gender):
        """Инициализируем атрибуты описания пользователя."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.gender = gender

    def describe_user(self):
        """Метод, который выводит сводку с информацией о пользователе."""
        print(f"Пользователь: \n{self.first_name} {self.last_name} ")
        print(f"Возраст: \n{self.age}")
        print(f"Пол: \n{self.gender}")

    def greet_user(self):
        """Вывод персонального приветствия для пользователя."""
        print(f"\nПриветствую, вас, {self.first_name} {self.last_name}!\n")

user_1 = User('alexey', 'polyachenko', 33, 'male')
user_1.describe_user()
user_1.greet_user()

user_2 = User('margarita', 'polyachenko', 27, 'female')
user_2.describe_user()
user_2.greet_user()