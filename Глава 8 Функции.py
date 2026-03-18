# Определение функции

# def greet_user():
#     """ Выводит простое приветствие. """
#     print("\nHello!")
#
# greet_user()

# Передача данных функции
#
# def greet_user(username):
#     """ Выводит простое приветствие. """
#     print(f"\nHello, {username.title()}!")
#
# greet_user('jessi')

# Позиционные аргументы

# def describe_pet(animal_type, pet_name):
#     """Выводит информацию о животном"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')

# Именованные аргументы

# def describe_pet(animal_type, pet_name):
#     """Выводит информацию о животном"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='harry', animal_type='hamster')

# Значения по умолчанию/Эквивалентные вызовы функций

# def describe_pet(pet_name, animal_type= 'dog'):
#     """Выводит информацию о животном"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
# # Собака Вилли.
# describe_pet('Willie')
# describe_pet(pet_name='Willie')
#
# # Хомяк Гарри.
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')

#  Возвращаемое значение / Возвращение простого значения

# def get_formatted_name(first_name, last_name):
#     """ возвращает отформатированное полное имя"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
# misician = get_formatted_name('jimmi', 'hendrix')
# print(misician)

# Необязательные аргументы

# def get_formatted_name(first_name, last_name, middle_name=''):
#     """ возвращает отформатированное полное имя"""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
# musician = get_formatted_name('jimmi', 'hendrix')
# print(musician)
#
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)

# Возвращение словаря

# def build_person(first_name, last_name, age=''):
#     """Возвращает словарь"""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
#
# musician = build_person('jimmi', 'hendrix', age=27)
# print(musician)

# Использование функции в цикле while
#
# def get_formatted_name(first_name, last_name):
#     """ возвращает отформатированное полное имя"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
# # Бесконечный цикл!
# while True:
#     print("\nPlease tell me your name: ")
#     print("(enter 'q' at any time to quit)")
#
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#
#     l_name = input("Last name: ")
#     if l_name =='q':
#         break
#
#     formatted_name = get_formatted_name(f_name,l_name)
#     print(f"\nHello, {formatted_name}!")

# Передача списка

# def greet_users(names):
#     """Выводит простое приветствие для каждого пользователя в списке"""
#     for name in names:
#         message = f"Hello, {name.title()}!"
#         print(message)
#
# usernames = ['hamaha', 'satoshi', 'evans']
# greet_users(usernames)

# Изменение списка в функции

# def print_models(unprinted_designs, completed_models):
#     """
#     Иммитирует печать моделей, пока список не станет пустым.
#     Каждая модель после печати перемещается в completed_models.
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)
#
# def show_completed_models(completed_models):
#     """Выводит информацию обо всех напечатанных моделях"""
#     print("\nThe following models have been printed:\n")
#     for completed_model in completed_models:
#         print(completed_model)
#
# unprinted_designs = ['phone case', 'robot pedant', 'dodecahedron']
# completed_models = []
#
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)