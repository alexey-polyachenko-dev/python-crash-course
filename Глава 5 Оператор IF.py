# Простой пример

# cars = ['audi', 'bmw', 'subaru', 'toyota']
#
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# Проверка равенства без учета регистра

# car = 'Audi'
# car.lower() == 'audi'
#
# print(car)

# Проверка неравенства

# requested_topping = 'mushrooms'
#
# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")

# Сравнение чисел

# answer = 17
# if answer != 42:
#     print("That is not the correct answer. Please try again!")

# Проверка отсутствия значения в списке

# banned_users = ['andrew', 'carolina', 'david']
# user = 'marie'
# if user not in banned_users:
#     print(f"{user.title()}, you can post a response if you wish.")

# Простые операторы if

# age = 17
# if age >= 18:
#     print("\nYou are old enough to vote")
#     print("Have you registered to vote yet?")
# else:
#     print("\nSorry, you are too young to vote.")
#     print("Please register to vote as soon as you turn 18!")

# Цепочки if-elif-else

# age = 65
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:
#     price = 40
# # else:
# #     price = 20
# elif age >= 65:
#     price = 20
# print(f"\nYour admission cost is ${price}.")

# Проверка нескольких условий

# request_toppings = ['mushrooms', 'extra cheese']
# if 'mushrooms' in request_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in request_toppings:
#     print("Adding pepperoni.")
# if 'extra cheese' in request_toppings:
#     print("Adding extra cheese.")
#
# print("\nFinished making your pizza!")

# Проверка специальных значений

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print(f"Adding {requested_topping}.")
#
# print("\nFinished making your pizza!")

# Проверка наличия содержимого в списке

# requested_toppings = []
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}.")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

# Множественные списки

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni','pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adiing {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")