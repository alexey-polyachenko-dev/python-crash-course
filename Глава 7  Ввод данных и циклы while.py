# Как работает функция input()

# promt = "If you share your name, we can personalize the messages you see."
# promt += "\nWhat is your first name? "
#
# name = input(promt)
# print(f"\nHello, {name.title()}!")

# Функция int() для получения числового ввода

# height = input("How tall are you, in inches? ")
# height = int(height)
#
# if height >= 48:
#     print("\You're tall enough to ride!")
# else:
#     print("\nYou're be able to ride when you're a little order.")

# Оператор деления по модулю

# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# # number = int(number)
# #
# # if number % 2 == 0:
# #     print(f"\nThe number {number} is even.")
# # else:
# #     print(f"\nThe number {number} is odd")

# Как работает цикл while

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# Пользователь решает прервать работу программы

# promt = "\nTell me something, and I will repeat it back to you:"
# promt += "\nEnter 'quit' to the end program.\n"
#
# message = ""
#
# while message != 'quit':
#     message = input(promt)
#
#     if message != 'quit':
#         print(message)

# Флаги

# promt = "\nTell me something, and I will repeat it back to you:"
# promt += "\nEnter 'quit' to the end program.\n"
#
# message = ""
# active = True
# while active:
#     if message == 'quit':
#         active = False
#     else:
#         print(message)
#         message = input(promt)

# Оператор break и выход из цикла

# promt = "\nPlease enter the name of a city you have visited:"
# promt += "\n(Enter 'quit' when you are finished.)\n"
#
# while True:
#     city = input(promt)
#
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

# Оператор continue и продолжение цикла

# curren_number = 0
# while curren_number < 10:
#     curren_number += 1
#     if curren_number % 2 == 0:
#         continue
#
#     print(curren_number)

# Предотвращение зацикливания

# x = 1
# while x <= 5:
#     print(x)
#     x += 1

# Перемещение элементов между списками

# # Начинаем с двух списков: пользователей, которых нужно проверить,
# # и пустого списка для хранения проверенных пользователей
# unconfirmed_users = ['alice', 'brien', 'candance']
# confirmed_users = []
#
# # Проверяем каждого пользователя, пока остаются непроверенные пользователи.
# # Каждый пользователь прошедший проверку, перемещается в список проверенных
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#
#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)
#
# # Вывод всех проверенных пользователей
# print(f"\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# Удаление всех вхождений конкретного значения из списка

# pets = ['dog', 'cat', 'fish', 'frog', 'cat', 'cat', 'bird', 'fox', 'cat']
# print(pets)
#
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

# Заполнение словаря данными, введенными пользователем

responses = {}
# Установка флага.
polling_active = True

while polling_active:
    # Запрос имени и ответа пользователя.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    # Ответ сохраняется в словаре.
    responses[name] = response

    # Проверка продолжения опроса.
    repeat = input("\nWould you like to let another person respond? (yes/ no) ")
    repeat = repeat.lower()
    if repeat == 'no':
        polling_active = False

# Опрос завершен, вывести результаты
print("\n--- Poll Result ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")