from random import choice

#Создаем список
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

print("Сейчас мы будем определять выйгрышную комбинацию:\n")

win_ticket = []

"""Цикл выполняется пока не определится 4 значения выйгрышной комбинации"""
while len(win_ticket) < 4:
    value = choice(list)
    """Цикл для исключения повторяющихся значений в комбинации"""
    if value not in win_ticket:
        print(f"Определяем комбинацию... Выбранное значение: {value}")
        win_ticket.append(value)

print(f"\nВыигрывает билет с комбинацией:"
      f"{win_ticket}")
