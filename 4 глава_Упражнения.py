#4.1 Pizza

# pizzas = ['pepperoni', 'calzone', '4 cheeses']
# for pizza in pizzas:
#     print(f"I like {pizza} pizza!")
#
# print("\nI really like pizza!\n")

#4.2 Animals

# animals = ['lion', 'zebra', 'monkey', 'crocodile', 'elephant']
# for animal in animals:
#     print(f"The {animal.title()} lives in Africa")
#
# print("\nThese animals can be see during Safari")

#4.3 Считаем до 20

# for value in range(1,21):
#     print(value)

#4.4 Миллион

# one_million = list(range(1,100001))
# for value in one_million:
#     print(value)

#4.5 Суммирование миллиона чисел

# one_million = list(range(1,1000001))
# print(f"{min(one_million)}\n{max(one_million)}\n{sum(one_million)}")

#4.6 Нечетные числа

# undead_numbers = list(range(1,21,2))
# for value in undead_numbers:
#     print(value)

#4.7 Тройки

# multiples = list(range(3,31,3))
# for value in multiples:
#     print(value)

#4.8 Кубы

# cubes = []
# for value in range(1,11):
#     cubes.append(value**3)
#     print(value**3)

#4.9 Генератор кубов

# cubes = [value**3 for value in range(1,11)]
# print(cubes)

#4.10 Срезы

# my_foods = ['pizza', 'falafel', 'carrot cake', ' patato', 'broccoli', 'cheese']
# print("Первые три пункта в списке - это:")
# print(my_foods[:3])
#
# print("\nТри пункта из середины списка - это:")
# print(my_foods[1:4])
#
# print("\nПоследние три пункта в списке - это:")
# print(my_foods[-3:])

# 4.11 Моя пицца, твоя пицца

# pizzas = ['pepperoni', 'calzone', '4 cheeses']
# friend_pizzas = pizzas[:]
#
# pizzas.append('roman')
# friend_pizzas.append('with a pear')
#
# print("My favorite pizza are:")
#
# for pizza in pizzas:
#     print(f"\t{pizza}")
#
# print("\nMy friend's favorite pizza are:")
#
# for pizza in friend_pizzas:
#     print(f"\t{pizza}")

#4.12 Больше циклов

# pizzas = ['pepperoni', 'calzone', '4 cheeses']
# friend_pizzas = pizzas[:]
#
# pizzas.append('roman')
# friend_pizzas.append('with a pear')
#
# print("My favorite pizza are:")
#
# for pizza in pizzas:
#     print(f"\t{pizza}")
#
# print("\nMy friend's favorite pizza are:")
#
# for pizza in friend_pizzas:
#     print(f"\t{pizza}")

# 4.13 Шведский стол

# buffet = ('cheese', 'meet', 'stake', 'fish', 'fruit')
# print("Original menu:\n")
# for dish in buffet:
#     print(f"{dish.title()}")
#
# buffet = ('milk', 'tea', 'cheese', 'meet', 'stake')
# print("\nModified menu:\n")
# for dish in buffet:
#     print(f"{dish.title()}")
