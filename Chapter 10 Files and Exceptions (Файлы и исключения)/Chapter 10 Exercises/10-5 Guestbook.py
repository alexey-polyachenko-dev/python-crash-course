from pathlib import Path

path = Path('guest.txt')
guestbook = ''

while True:
    guest_name = input("Enter your name:\n"
                       "(to exit, enter 'q')\n")
    if guest_name == 'q':
        break

    else:
        print(f"Hello, {guest_name.title()}! You have been added to the guestbook.\n")
        guestbook += f"{guest_name.title()}\n"

path.write_text(guestbook)