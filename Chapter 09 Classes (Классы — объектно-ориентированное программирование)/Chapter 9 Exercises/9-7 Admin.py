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

class Admin(User):
    """Потомок класса User"""

    def __init__(self, first_name, last_name, age, gender):
        """Инициализирует атрибуты класса родителя.
        Затем инициализируем атрибуты, спецефические для администратора."""
        super().__init__(first_name, last_name, age, gender)
        self.privileges = []

    def show_privileges(self):
        """Выводит права администратора."""
        print(f"Администратор, {self.first_name} {self.last_name}, обладает"
              f" следующими правами:")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin = Admin('jack', 'jonson', 33, 'male')
admin.privileges = ['разрешено добавлять сообщения',
                    'разрешено удалять пользователей',
                    'разрешено банить пользователей']
admin.show_privileges()