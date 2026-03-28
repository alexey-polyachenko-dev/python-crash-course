# 5.3 Цвета пришельцев 1

# alien_color = 'red'
#
# if alien_color == 'green':
#     print("\nYou won 5 points")

# 5.4 Цвета пришельцев 2

# alien_color = 'rec'
# if alien_color == 'green':
#     print("\nYou won 5 points")
# else:
#     print("\nYou won 10 points")

# 5.5 Цвета пришельцев 3

# alien_color = 'yellow'
# if alien_color == 'green':
#     print("\nYou won 5 points")
# elif alien_color == 'yellow':
#     print("\nYou won 10 points")
# else:
#     print("\nYou won 15 points")

# 5.6 Периоды жизни
# v1
# age = 100
# if age < 2:
#     print("младенец")
# if age >= 2 and age <4:
#     print("малыш")
# if age >=4 and age < 13:
#     print("ребенок")
# if age >= 13 and age < 20:
#     print("подросток")
# if age >= 20 and age < 65:
#     print("взрослый")
# if age >=65:
#     print("пожилой человек")

#v2
# age = 100
# if age < 2:
#     print("младенец")
# elif age < 4:
#     print("малыш")
# elif age < 13:
#     print("ребенок")
# elif age < 20:
#     print("подросток")
# elif age < 65:
#     print("взрослый")
# elif age >= 65:
#     print("пожилой человек")

# 5.7 Любимый фрукт

# favorite_fruit = ['strawberries', 'orange', 'kiwi']
# if 'banana' in favorite_fruit:
#     print("You like bananas")
# if 'strawberries' in favorite_fruit:
#     print("You like strawberries")
# if 'apple' in favorite_fruit:
#     print("You like apple")
# if 'orange' in favorite_fruit:
#     print("You like oranges")
# if 'kiwi' in favorite_fruit:
#     print("You like kiwi")

# 5.8 Здравствуйте, админ!

# usernames = ['alex', 'bob', 'celena', 'den', 'elena', 'frank', 'admin']
# for username in usernames:
#     if username == 'admin':
#         print(f"Здравствуйте, {username}, хотите посмотреть отчет о сосотоянии дел?")
#     else:
#         print(f"Привет, {username}, спасибо, что авторизовался в системе!")

# 5.9 Нет пользователей

# usernames = []
# if usernames:
#     for username in usernames:
#         if username == 'admin':
#             print(f"\nЗдравствуйте, {username}, хотите посмотреть отчет о сосотоянии дел?")
#         else:
#             print(f"Привет, {username}, спасибо, что авторизовался в системе!")
# else:
#     print("Нам нужно добавить несколько пользователей!")

# 5.10 Проверка имен пользователей

# current_users = ['aLex', 'BoB', 'Celena', 'deN', 'Elena', 'fraNk']
# new_users = ['ben', 'crisp', 'bOb', 'janet', 'DEn']
# current_users_low = [user.lower() for user in current_users]
# for new_user in new_users:
#     if new_user.lower() in current_users_low:
#         print(f"{new_user.lower()} уже занято, выберите новое имя.")
#     else:
#         print(f"Имя, {new_user.lower()}, доступно.")

# 5.11 Порядковые числительные

numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")