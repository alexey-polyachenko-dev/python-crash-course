from pathlib import Path

guest_name = input("Enter your name:\n")
path = Path('guest.txt')
path.write_text(guest_name)

