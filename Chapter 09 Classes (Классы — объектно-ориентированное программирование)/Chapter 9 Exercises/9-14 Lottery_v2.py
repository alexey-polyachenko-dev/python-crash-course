from random import choice

#Создаем список
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

print("Сейчас мы будем определять выйгрышную комбинацию:\n")

win_ticket = []
for _ in range(4):
    value_ticket = choice(list)
    win_ticket.append(value_ticket)
    print(f"Определяем комбинацию.... Выбраное значение: {value_ticket}")

print(f"\nВыигрывает билет с кобинацией:\n"
      f"{win_ticket}")