# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")
#
# print("Thank you, everyone. That was a great magic show!")
#
# for value in range(6):
#     print(value)
#
# number = list(range(6))
# print(number)
#
# even_number = list(range(2,11,2))
# print(even_number)
#
# digits = []
# for value in range(10):
#     digits.append(value)
#
# print(min(digits), max(digits), sum(digits))

#Генераторы списков

# squares = [value**2 for value in range(1,11)]
# print(squares)

# Нарезка списков

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:4])

# Перебор содержимого среза

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print("Here are the first three players on my team:")
# for player in players[:3]:
#     print(f"{player.title()}")

# Копирование списка

# my_foods = ['pizza', 'falafel', 'carrot cake', ' patato', 'broccoli', 'cheese']
# friend_foods = my_foods[:]
# my_foods.append('cannoli')
# friend_foods.append('ice cream')
#
# print("My favorite foods are:")
# print(my_foods)
#
# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# Кортежи

# dimensions = (200,50)
# print("Original dimensions:")
# for dimension in dimensions:
#     print(dimension)
#
# dimensions = (400,100)
# print("\nModified dimensions:")
# for dimension in dimensions:
#     print(dimension)