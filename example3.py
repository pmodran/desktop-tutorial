import random

choices = ('r','p','s')


while True:
    play_state = input("Welcome to Rock, Paper, Scissors! do you want to play?(y/n) ").lower()
    if play_state == 'n':
        print("Ok, BYE!!!!")
        break
    elif play_state != 'y':
        print("Invalid input")
        continue
    player = input("Enter 'r' for rock, 'p' for paper, and 's' for scissors: ").lower()
    if player not in choices:
        print('Invalid choice!')
        continue 
    

    computer = random.choice(choices)
    # 1 = rock, 2 = paper, 3 = scissor
    match computer:
        case 'r':
            print("Computer chose 🪨")
            match player:
                    case 'r':
                        print("You drew")
                    case 'p':
                        print("You WIN!!!")
                    case 's':
                        print("You LOSE :( ✂️")
        case 'p':
            print("Computer chose📄")
            match player:
                    case 'r':
                        print("You LOSE :( ✂️")
                    case 'p':
                        print("You drew")
                    case 's':
                        print("You WIN!!!")
        case 's':
            print("Computer chose ✂️")
            match player:
                    case 'r':
                        print("You WIN!!!")
                    case 'p':
                        ("You LOSE :(  ")
                    case 's':
                        print("You drew")



    

  