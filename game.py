while True:
    print( "*****Rock Paper Scissor Game****")
    import random
    comp = random.randint(1,3)
    if comp == 1:
        computer = 'r'
    elif comp == 2:
        computer = 'p'
    else:
        computer = 's'
    player = input("Enter 'r' for rock, 's' for scissor, 'p' for paper: ")
    if player == 'r':
        if computer == 's':
            print("You win ")
        elif computer == 'p': 
            print("You Lose ")
        else:
            print("It is a tye! Try again")
    elif player == 'p':
        if computer == 'r':
            print("You win ")
        elif computer == 's': 
            print("You Lose ")
        else:
            print("It is a tye! Try again")
    elif player == 's':
        if computer == 'p':
            print("You win ")
        elif computer == 'r': 
            print("You Lose ")
        else:
            print("It is a tye! Try Again ")
    else:
        print("It is tye! Try again ")
    print(f"Computer enter {computer}, You enter {player}")
    play_again = input("Play again? (yes/no): ")
    if play_again.lower() != "yes":
        break