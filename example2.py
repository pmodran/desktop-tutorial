import random

x = random.randint(1,100)
while True:
    y = int(input("Guess a number between 1 and 100: "))
    if (x == y):
        print("You Guessed Right!!!")
        break
    elif(x < y):
        print("Too High")
    elif(x > y):
        print("Too Low")
    else:
        print ("Invalid number")