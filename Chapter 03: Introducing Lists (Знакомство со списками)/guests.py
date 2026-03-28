guests = ['Alex', 'Ben', 'Cris']
print(f"{guests[0]}, приглашаю Вас на обед!\n{guests[1]}, приглашаю Вас на обед!\n{guests[2]}, приглашаю Вас на обед!")

print(f"\nК сожалению, {guests[1]}, не сможет к нам присоединиться!\n")

del guests[1]
guests.insert(1, 'Jack')
print(f"{guests[0]}, приглашаю Вас на обед!\n{guests[1]}, приглашаю Вас на обед!\n{guests[2]}, приглашаю Вас на обед!\n")

print("Хорошие новости! У меня появился стол побольше и теперь я могу пригласить ещё гостей!")

guests.insert(0, 'Victotia')
guests.insert(2, 'Anna')
guests.append('Linda')

print(f"\nТеперь гостей будет: {len(guests)}\n")

print(f"{guests[0]}, приглашаю Вас на обед!\n{guests[1]}, приглашаю Вас на обед!\n{guests[2]}, приглашаю Вас на обед!\n{guests[3]}, приглашаю Вас на обед!\n{guests[4]}, приглашаю Вас на обед!\n{guests[5]}, приглашаю Вас на обед!\n")

print("Друзья, я смогу принять всего два гостя!")

popped_guest = guests.pop()
print(f"\n{popped_guest}, я сожалею, но приглашение для Вас отменяется")
popped_guest = guests.pop()
print(f"{popped_guest}, я сожалею, но приглашение для Вас отменяется")
popped_guest = guests.pop()
print(f"{popped_guest}, я сожалею, но приглашение для Вас отменяется")
popped_guest = guests.pop()
print(f"{popped_guest}, я сожалею, но приглашение для Вас отменяется")

print(f"\n{guests[0]}, приглашение для Вас остается актуальным!\n{guests[1]}, приглашение для Вас остается актуальным!")

del guests[1]
del guests[0]

print(guests)