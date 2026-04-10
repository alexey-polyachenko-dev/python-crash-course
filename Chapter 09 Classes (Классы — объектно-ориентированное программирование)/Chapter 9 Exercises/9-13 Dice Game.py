from random import randint

class Dice:
    """Создаем класс кубика с значением граней по умолчанию"""
    def __init__(self, sides = 6):
        """Инициализируем атрибут описания кубика"""
        self.sides = sides

    def roll_die(self):
        """Создаем метод для вывода случайного числа от 1 до количества
        граней на кубике"""
        return randint(1, self.sides)


#Кубик имеет 6 граней
a6 = Dice()
results = []

for _ in range(10):
    throw = a6.roll_die()
    results.append(throw)

print(f"Результаты 10 бросков кубика с 6 гранями: \n{results}")

#Кубик имеет 10 граней
a10 = Dice(10)
results = []

for _ in range(10):
    throw = a10.roll_die()
    results.append(throw)

print(f"\nРезультаты 10 бросков кубика с 10 гранями: \n{results}")

#Кубик имеет 20 граней
a20 = Dice(10)
results = []

for _ in range(10):
    throw = a20.roll_die()
    results.append(throw)

print(f"\nРезультаты 10 бросков кубика с 20 гранями: \n{results}")