from random import choice

def generate_ticket(list):
    """Функция генерации лотерейных билетов"""
    ticket = []
    while len(ticket) < 4:
        element = choice(list)
        """Условие не повторения элементов в комбинации"""
        if element not in ticket:
            ticket.append(element)
    return ticket

def ticket_comparison(winning_ticket, new_ticket):
    """Функция сравнения выйгрышного и участвующего в игре билета"""
    for element in new_ticket:
        if element not in winning_ticket:
            return False
    return True

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_ticket = generate_ticket(list)

won = False
count = 0
max_tries = 1_000_000

while not won:
    new_ticket = generate_ticket(list)
    count +=1
    won= ticket_comparison(winning_ticket, new_ticket)
    if count >= max_tries:
        break

if won:
    print("\nПоздравляем, вы, выйграли!")
    print(f"Победная комбинация - {winning_ticket}")
    print(f"Комбинация вашего билета - {new_ticket}")
    print(f"Для победы вам понадобилось {count} попыток.")
else:
    print(f"\nВы использовали {count} попыток! Игра закончена!")
    print(f"Победная комбинация была - {winning_ticket}")
    print(f"Ваш билет - {new_ticket}")
    print("Удачи в следующей игре!")