from random import choice

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

def get_single_ticket(list):
    """Функция генерации лотерейного билета"""
    ticket = []
    while len(ticket) < 4:
        value = choice(list)
        """Исключаем повторения значений в комбинации"""
        if value not in ticket:
            ticket.append(value)
    return ticket

"""Определяем выйгрышный билет"""
winning_ticket = get_single_ticket(list)

iterations = 0
"""Цикл для определения количества попыток для генерации выйгрышного билета"""
while True:
    my_ticket = get_single_ticket(list)
    iterations += 1
    """Условие, которое указывает на то,
    что нам не важен порядок символов в комбинации"""
    if set(winning_ticket) == set(my_ticket):
        break

print(f"Выйгрышная комбинация - {winning_ticket}")
print(f"Мой лотерейный билет - {my_ticket}")
print(f"Понадобилось {iterations} попыток!")