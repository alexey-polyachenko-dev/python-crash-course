import class_user

class Admin(class_user.User):
    """Потомок класса User"""

    def __init__(self, first_name, last_name, age, gender):
        """Инициализирует атрибуты класса родителя.
        Затем инициализируем атрибуты, спецефические для администратора."""
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()


class Privileges:
    """Создаем класс Privileges."""
    def __init__(self, privileges=[]):
        """Инициализируем атрибут"""
        self.privileges = privileges

    def show_privileges(self):
        """Выводит права администратора."""
        print("\nПользователь обладает следующими правами:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("---")