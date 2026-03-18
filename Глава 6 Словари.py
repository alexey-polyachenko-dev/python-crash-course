# Обращение к значениям в словаре

# alien_0 = {'color' : 'green', 'points' : 5}
# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")

# Добавление новых пар "ключ - значение"

# alien_0 = {'color' : 'green', 'points' : 5}
# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# Создание пустого словаря

# alien_0 = {}
#
# alien_0['color'] = 'green'
# alien_0['points'] = 5
#
# print(alien_0)

# Изменение значений в словаре

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original position: {alien_0['x_position']}")
# alien_0['speed'] = 'fast'
#
# # Пришелец перемещается вправою
# # Вычисляем величину смещения на основе текущей скорости
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     # пришелец двигается быстро
#     x_increment = 3
#
# # Новая позиция ровна сумме старой позиции и приращения.
# alien_0['x_position'] = alien_0['x_position'] + x_increment
#
# print(f"New position: {alien_0['x_position']}")

# Удаление пар "ключ - значение

# alien_0 = {'color' : 'green', 'points' : 5}
# print(alien_0)
#
# del alien_0['points']
# print(alien_0)

# Словарь с однотипными объектами

# favorite_languages = {
#     'jen' : 'python',
#     'sarah' : 'c',
#     'edward' : 'rust',
#     'phil' : 'python',
#     }
#
# language = favorite_languages['sarah'].title()
# print(f"\nSarah's favorite language is {language}")

# Обращение к значениям методом get()

# alien_0 = {'color' : 'green', 'speed' : 'slow'}
# points_value = alien_0.get('points', 'No point value assigned.')
# print(points_value)

# Перебор всех пар "ключ - значение"

# user_0 = {
#     'username' : 'efermi',
#     'first' : 'enrico',
#     'last' : 'fermi'
#     }
#
# for key, value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")

# Перебор всех ключей в словаре

# favorite_languages = {
#     'jen' : 'python',
#     'sarah' : 'c',
#     'edward' : 'rust',
#     'phil' : 'python',
#     }
#
# if 'eric' not in favorite_languages.keys():
#     print("\nEric, please take our poll!\n")
#
# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}.")
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}'s, I see you love {language}!")

# Перебор ключей словаря в определенном порядке

# favorite_languages = {
#     'jen' : 'python',
#     'sarah' : 'c',
#     'edward' : 'rust',
#     'phil' : 'python',
#     }
#
# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

# Перебор всех значений в словаре

# favorite_languages = {
#     'jen' : 'python',
#     'sarah' : 'c',
#     'edward' : 'rust',
#     'phil' : 'python',
#     }
#
# print("\nThe following language have been mentioned:\n")
# for language in set(favorite_languages.values()):
#     print(language.title())

# Список словарей

# alien_0 = {'color' : 'green', 'points' : 5}
# alien_1 = {'color' : 'yellow', 'points' : 10}
# alien_2 = {'color' : 'red', 'points' : 15}
#
# aliens = [alien_0, alien_1, alien_2]
#
# for alien in aliens:
#     print(alien)

# # Создание пустого списка для хранения данных о пришельцах
# aliens = []
#
# # Создание 30 зеленых пришельцев
# for alien_number in range(30):
#     new_alien = {'color':'green', 'points':5, 'speed':'slow'}
#     aliens.append(new_alien)
#
# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
#
# # вывод данных о первых пяти пришельцах:
# for alien in aliens[:5]:
#     print(alien)
# print("...")
#
# # вывод количества созданных пришельцев
# print(f"Total nuber of aliens: {len(aliens)}")

# Список в словаре

# # сохранение информации о заказанной пицце
# pizza = {
#     'crust': 'trick',
#     'toppings': ['mushrooms', 'extra cheese']
#     }
# # описание заказа
# print(f"You ordered a {pizza['crust']}-crust pizza"
#       "with the following toppings:")
#
# for topping in pizza['toppings']:
#     print(f"\t{topping}")

# favorite_languages = {
#     'jen' : ['python', 'rust'],
#     'sarah' : ['c'],
#     'edward' : ['rust', 'go'],
#     'phil' : ['python', 'haskel'],
#      }
#
# for name, languages in favorite_languages.items():
#     if len(languages) == 1:
#         print(f"\n{name.title()}'s favorite language are:")
#     else:
#         print(f"\n{name.title()}'s favorite languages are:")
#     for language in languages:
#         print(f"\t{language.title()}")

# Вложение словарей

users = {
    'aeinstein' : {
        'first' : 'albert',
        'last' : 'einstein',
        'location' : 'princeton'
        },

    'mcurie' : {
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris'
        }
    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")