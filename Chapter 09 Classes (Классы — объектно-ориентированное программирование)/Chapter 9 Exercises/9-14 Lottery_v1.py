from random import choice

class Lottery:
      """Создаем класс лотерея"""

      def __init__(self):
            """Инициализируем атрибуты лотереи"""
            self.list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
            self.win_ticket = [1, 'a', 3, 'c']
            self.ticket = []

      def lottery_ticket(self):
            """Метод для генерации лотерейных билетов"""
            self.number_1 = choice(self.list)
            self.ticket.append(self.number_1)
            self.number_2 = choice(self.list)
            self.ticket.append(self.number_2)
            self.number_3 = choice(self.list)
            self.ticket.append(self.number_3)
            self.number_4 = choice(self.list)
            self.ticket.append(self.number_4)

            print(
                  f"Выйгрышным считается билет собравший данную комбинацию: "
                  f"{self.win_ticket}"
                  f"\nКомбинация вашего лотерейного билета: {self.ticket}\n")

my_ticket = Lottery()
my_ticket.lottery_ticket()