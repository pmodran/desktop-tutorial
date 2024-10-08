import random

while True:
    x = input("Do you want to roll the dice?(y/n): ").lower()

    if x == 'y':
        a = random.randint(1,6)
        b = random.randint(1,6)
        print(f'({a},{b})')
    elif x == 'n':
        print("Goodbye!")
        break
    else:
        print("Invalid input")





