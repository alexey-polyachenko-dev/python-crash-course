class User:
    """Создаем класс User."""

    def __init__(self, first_name, last_name, age, gender):
        """Инициализируем атрибуты описания пользователя."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        """Метод, который выводит сводку с информацией о пользователе."""
        print(f"Пользователь: \n{self.first_name} {self.last_name} ")
        print(f"Возраст: \n{self.age}")
        print(f"Пол: \n{self.gender}")

    def greet_user(self):
        """Вывод персонального приветствия для пользователя."""
        print(f"\nПриветствую, вас, {self.first_name} {self.last_name}!\n")

    def increment_login_attempts(self):
        """Метод, увеличивающий значение login_attempts на 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Метод, который обнуляет значение login_attempts."""
        self.login_attempts = 0

user_1 = User('alexey', 'polyachenko', 33, 'male')

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(f"\nКоличество входов: {user_1.login_attempts}\n")

user_1.reset_login_attempts()
print(f"\nКоличество входов: {user_1.login_attempts}\n")