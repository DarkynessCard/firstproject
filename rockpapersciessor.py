'''first import random for the random choice
then make a list countaining the options
introduce the player to the game
create random choice
then do the logic'''


def rock():
    import random
    choices = ["rock", "paper", "scissors"]
    print("Welcome to rock, paper, scissors")
    while True:
        user_choice = input("Enter an option; rock, paper, or scissors(or 'quit') to stop\n").lower()

        if user_choice == 'quit':
            print("Thank you for playing")
            break

        if user_choice not in choices:
            print("Please enter a correct choice, try again")
            continue
        computer_choice = random.choice(choices)
        print(f"Computer choses : {computer_choice}")
        if user_choice == computer_choice:
            print("You tie")
        elif (
                (user_choice == "rock" and computer_choice == "scissors") \
                or (user_choice == "paper" and computer_choice == "scissors") \
                or (user_choice == "scissors" and computer_choice == "rock")):
            print("You win")
        else:
            print("You lose")


rock()
