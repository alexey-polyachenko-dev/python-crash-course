phones = ['apple', 'sony', 'xiomi', 'samsung', 'lg']
print(phones)

print(phones[0])
print(phones[-1])

message = f"My first phone was a {phones[1].title()}"
print(message)

phones[-1] = 'huawei'
print(phones)

phones.append('lg')
print(phones)

phones.insert(3, 'meizu')
print(phones)

del phones[3]
print(phones)

popped_phones = phones.pop()
print(phones)
print(popped_phones)

phones.remove('xiomi')
print(phones)

too_expensive = 'apple'
phones.remove(too_expensive)
print(f"A {too_expensive.upper()} is too expensive for me!")

phones.sort()
print(phones)

phones.sort(reverse=True)
print(phones)

phones.append('apple')
print(phones)

print(sorted(phones))
print(sorted(phones, reverse=True))
print(phones)

phones.reverse()
print(phones)

len(phones)