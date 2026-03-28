# 6.1 Персона

# persona = {
#     'first_name' : 'Jack',
#     'last_name' : 'Clinton',
#     'age' : 47,
#     'city' : 'LA'
#     }
# print(persona)

# 6.2 Любимые числа

# favorite_numbers = {
#     'stas' : 25,
#     'alexandr' : 7193,
#     'alexey' : 5,
#     'grisha' : 13,
#     'boris' : 17
#     }
# print(f"\nStas favorite number : {favorite_numbers['stas']}")
# print(f"Alexandr favorite number : {favorite_numbers['alexandr']}")
# print(f"Alexey favorite number : {favorite_numbers['alexey']}")
# print(f"Grisha favorite number : {favorite_numbers['grisha']}")
# print(f"Boris favorite number : {favorite_numbers['boris']}")

# 6.3 Глоссарий

# gloss = {
#     'переменная' : 'хранит значение, то есть связанные с ней данные.',
#     'строка' : 'представляет собой простую последовательность символов.',
#     'константа' : 'представляет собой переменную, значение которой остается'
#                   ' неизменным на протяжении всего срока жизни программы.',
#     'список' : 'набор элементов, следующих в определенном порядке',
#     'кортеж' : 'список элементов, который не может изменяться'
#     }
# print(f"\nПеременная - {gloss['переменная']}")
# print(f"\nСтрока - {gloss['строка']}")
# print(f"\nКонстанта - {gloss['константа']}")
# print(f"\nСписок - {gloss['список']}")
# print(f"\nКортеж - {gloss['кортеж']}")

# 6.4 Глоссарий 2

# gloss = {
#     'Переменная' : 'хранит значение, то есть связанные с ней данные.',
#     'Строка' : 'представляет собой простую последовательность символов.',
#     'Константа' : 'представляет собой переменную, значение которой остается'
#                   ' неизменным на протяжении всего срока жизни программы.',
#     'Список' : 'набор элементов, следующих в определенном порядке',
#     'Кортеж' : 'список элементов, который не может изменяться',
#     'PEP' : 'Python Enhancement Proposal предложение по улучшению Python.',
#     'Словарь' : 'структура данных, предназначенная для объединения взаимосвязанной информации.',
#     'Множество' : 'похоже на список, но все его элементы должны быть уникальными.'
#     }
#
# for key, value in gloss.items():
#     print(f"{key} - {value}")

# 6.5 Реки

# rivers = {
#     'Ушачка' : 'Ушачи',
#     'Витьба' : 'Витебск',
#     'Полота' : 'Полоцк',
#     'Неман' : 'Гродно',
#     'Днепр' : 'Могилев',
#     'Сож' : 'Гомель',
#     'Свислочь' : 'Минск'
#     }
#
# for river, city in rivers.items():
#     print(f"Река {river} протекает через {city}.")
#
# for river in rivers.keys():
#     print(f"\tРека - '{river}'.")
#
# for city in rivers.values():
#     print(f"\t\tГород - '{city}'.")

# 6.6 Опрос

# favorite_languages = {
#     'jen' : 'python',
#     'sarah' : 'c',
#     'edward' : 'rust',
#     'phil' : 'python',
#      }
#
# peoples = ['alex', 'edward', 'linda', 'phil', 'peter', 'anna', 'jen', 'sarah']
#
# for people in peoples:
#     if people in favorite_languages.keys():
#         print(f"{people.title()}, спасибо, что приняли участие в опросе!")
#     else:
#         print(f"\t{people.title()}, пожалуйста, примите участие в опросе!")

# 6.7 Люди

# jclinton = {
#     'first_name' : 'Jack',
#     'last_name' : 'Clinton',
#     'age' : 47,
#     'city' : 'LA'
#     }
#
# alincoln = {
#     'first_name' : 'Avram',
#     'last_name' : 'Lincoln',
#     'age' : 69,
#     'city' : 'Washington'
#     }
#
# bmarley = {
#     'first_name' : 'Bob',
#     'last_name' : 'Marley',
#     'age' : 41,
#     'city' : 'Texas'
# }
#
# peoples = [jclinton, alincoln, bmarley]
#
# for people in peoples:
#     print(people)

# 6.8 Домашние животные

# bobik = {
#     'type' : 'dog',
#     'owner' : 'Elena'
#     }
#
# black = {
#     'type' : 'cat',
#     'owner' : 'Leonid'
#     }
#
# mars = {
#     'type' : 'bird',
#     'owner' : 'Cail'
#     }
#
# pets = [bobik, black, mars]
#
# for pet in pets:
#     print(pet)

# 6.9 Любимые места

# favorite_places = {
#     'mark' : ['red sea', 'hawaii'],
#     'bil' : ['black sea'],
#     'maria' : ['maldivi', 'bratislava', 'borviha']
#     }
#
# for person, places in favorite_places.items():
#     print(f"\n{person.title()} likes the following place:")
#     for place in places:
#         print(f"- {place.title()}")

# 6.10 Любимые числа

# favorite_numbers = {
#     'stas' : [25, 13],
#     'alexandr' : [7193, 1, 5],
#     'alexey' : [5],
#     'grisha' : [13, 1],
#     'boris' : [17]
#     }
#
# for name, numbers in favorite_numbers.items():
#     if len(numbers) == 1:
#         print(f"\n{name.title()} likes the number:")
#         for number in numbers:
#             print(f"\t {number}")
#     else:
#         print(f"\n{name.title()} likes numbers:")
#         for number in numbers:
#             print(f"\t{number}")

# 6.11 Города

# cities = {
#     'LA' : {
#         'country' : 'USA',
#         'population' : '3 850 000',
#         'fact' : 'HOLLYWOOD'
#         },
#     'Paris' : {
#         'country' : 'France',
#         'population' : '2 050 000',
#         'fact' : 'Rue des Derges Street'
#         },
#     'Minsk' : {
#         'country' : 'Belarus',
#         'population' : '1 996 730',
#         'fact' : 'Fenix City'
#         }
#     }
#
# for city, informations in cities.items():
#     print(f"\nBriefly about the city of {city}:")
#
#     country = informations['country']
#     print(f"\tCountry - {country}")
#     population = informations['population']
#     print(f"\tPopulation - {population}")
#     fact = informations['fact']
#     print(f"\tFact - {fact}")
