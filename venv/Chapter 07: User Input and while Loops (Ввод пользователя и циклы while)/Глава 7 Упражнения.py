# 7.1 Каршеринг

# message = input("\nКакую машину Вы хотели бы взять на прокат? \n")
# print(f"Посмотрим, смогу ли я найти вам {message.title()}.")

# 7.2 Заказ стола

# table = input("\nНа скольких человек вы хотели бы заказать столик? ")
# table = int(table)
#
# if table > 8:
#     print("\nИзвините, вам придется подождать.")
# else:
#     print("\nВаш столик готов!")

# 7.3 Числа, кратные 10

# promt = 'Давайте узнаем, кратно ли число 10!'
# promt += '\nВведите число:\n'
# number = input(promt)
# number = int(number)
#
# if number % 10 == 0:
#     print("\nКратно")
# else:
#     print("\nНе кратно")

# 7.4 Начинки для пиццы

# v.1 завершение цикла при проверке условия в операторе while

# promt = 'Какую начинку вы хотите добавить для вашей пиццы?'
# promt += "\n(Введите 'quit' если завершили выбор)\n"
#
# topping = ""
# while topping != 'quit':
#     topping = input(promt)
#
#     if topping != 'quit':
#         print(f"{topping.title()} добавлен(-а) в заказ!\n")

# 7.5 Билеты в кино

# promt = "\nВведите свой возраст, чтобы узнать стоимость билет:"
# promt += "\n(Напишите 'quit' для завершения)\n"
#
# while True:
#     age = input(promt)
#     if age == 'quit':
#         break
#     else:
#         age = int(age)
#         if age < 3:
#             price = 0
#         elif age >= 3 and age <= 12:
#             price = 10
#         elif age > 12:
#             price = 15
#         print(f"Стоимость билета будет составлять ${price}\n")

# 7.6 Три выхода

# v.2 управление продолжительностью цикла в зависимости от пременной active

# promt = 'Какую начинку вы хотите добавить для вашей пиццы?'
# promt += "\n(Введите 'quit' если завершили выбор)\n"
#
# toppings = ""
# active = True
# while active:
#     if toppings == 'quit':
#         active = False
#     else:
#         toppings = input(promt)
#         if toppings != 'quit':
#             print(f"{toppings.title()} добавлен(-а) в заказ!\n")

# v.3 выход из цикла с помощью оператора break,
# если пользователь вводит значение 'quit'

# promt = 'Какую начинку вы хотите добавить для вашей пиццы?'
# promt += "\n(Введите 'quit' если завершили выбор)\n"
#
# while True:
#     toppings = input(promt)
#     if toppings == 'quit':
#         break
#     else:
#         print(f"{toppings.title()} добавлен(-а) в заказ!\n")

# 7.8 Бутерброды

# sandwich_orders = ['бутерброд с колбасой', 'бутерброд с тунцом',
#                    'бутерброд с колбасой', 'бутерброд с сыром',
#                    'бутерброд с колбасой', 'бутерброд с вялеными томатами']
# finished_sandwich = []
#
# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     finished_sandwich.append(sandwich)
#     print(f"Я готовлю {sandwich}")
#
# print("\n")
#
# for sandwich in finished_sandwich:
#     print(f"Я приготовил {sandwich}")

# 7.9 Без колбасы

# sandwich_orders = ['бутерброд с колбасой', 'бутерброд с тунцом',
#                    'бутерброд с колбасой', 'бутерброд с сыром',
#                    'бутерброд с колбасой', 'бутерброд с вялеными томатами']
# finished_sandwich = []
#
# print("Бутербродов с колбасой больше нет")
#
# while 'бутерброд с колбасой' in sandwich_orders:
#     sandwich_orders.remove('бутерброд с колбасой')
# print(sandwich_orders)

# 7.10 Отпуск мечты

name_promt = 'Как вас зовут?\n'
place_promt = 'Если бы у вас была возможность посетить одно место в мире, куда бы отправились?\n'
cancel_promt = "Желаете продолжить опрос? ( да / нет )\n"
result_promt = '\n --- Результаты опроса --- \n'

places = {}
flag = True

while flag:
    name = input(name_promt)
    place = input(place_promt)
    places[name] = place

    cancel = input(cancel_promt)
    cancel = cancel.lower()

    if cancel == 'нет':
        flag = False

print(result_promt)

for name, place in places.items():
    print(f"{name.title()} хотел бы посетить {place.title()}.")