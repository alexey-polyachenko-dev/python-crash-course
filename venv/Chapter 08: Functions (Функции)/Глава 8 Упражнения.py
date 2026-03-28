# 8.1 Сообщение

# def display_message():
#     print("\nЧасть I. Основы "
#           "\nГлава 8. Функции")
#
# display_message()

# 8.2 Любимая книга

# def favotite_book(book):
#     print(f"\nОдна из моих любимых книг - '{book.title()}'.\n")
#
# favotite_book('алиса в стране чудес')

# 8.3 Футболка

# def make_shirt(size, text):
#     """Выводит размер футболки и текст на ней"""
#     print(f"Размер футболки {size}. Надпись на футболке - '{text}'\n")
#
# make_shirt('S', 'Just do it')
# make_shirt(size='S', text='Just do it')

# 8.4 Большие футболки

# def make_shirt(text, size='L'):
#     """Выводит размер футболки и текст на ней"""
#     print(f"\nРазмер футболки {size}. Надпись на футболке - '{text}'\n")
#
# make_shirt('Я люблю Python')
# make_shirt(size='M', text='Arsenal')

# 8.5 Города

# def describe_city(city, country='belarus'):
#     print(f"{city.title()} находится в {country.title()}")
#
# describe_city('Minsk')
# describe_city(city='Vitebsk')
# describe_city('moscow', 'russia')

# 8.6 Названия городов

# def city_country(city, country):
#     message = f"The city of {city} is located in {country}\n"
#     return message.title()
#
# couple = city_country('minsk', 'belarus')
# print(couple)
#
# couple = city_country('moscow', 'russia')
# print(couple)
#
# couple = city_country('kiev', 'ukraine')
# print(couple)

# 8.7 Альбом

# def make_album(artist, name_album, number_tracks=''):
# #     """Возвращает словарь с информацией об альбоме"""
# #     album = {'artist' : artist, 'name' : name_album}
# #     if number_tracks:
# #         album['number of tracks'] = number_tracks
# #     return album
# #
# # musician = make_album('baskov', 'rose', number_tracks= 13)
# # print(musician)
# #
# # musician = make_album('kirkorov', 'snow', number_tracks= 10)
# # print(musician)
# #
# # musician = make_album('instasamka', 'bitch', number_tracks= 7)
# # print(musician)

# 8.8 Пользовательские альбомы

def make_album(artist, name_album, number_tracks=0):
    album = {
        'artist' : artist.title(),
        'name of album' : name_album.title()
        }

    if number_tracks:
        album['number of tracks'] = number_tracks
    return album

while True:

    print("\nПожалуйста, введите данные об альбоме: ")
    print("(введите 'й' для выхода)")

    in_artist = input("Введите исполнителя: ")
    if in_artist == 'q':
        break

    in_name = input("Введите название альбома: ")
    if in_name == 'q':
        break

    build_album = make_album(in_artist,in_name)
    print(build_album)

