
'''The computer picks a random number from 1 to 100.

The user has limited attempts (e.g. 7) to guess the number.

After each guess, the program gives feedback: too high, too low, or correct.

If the user guesses the number in time, they win; otherwise, the number is revealed.


1. Create a variable to store randomly generated umbers range1-100
2. Create a variable to store player's guessed number
3. Create a counter to count the number of times the play attempted
4. Create a variable to store total allowed attempts
5. Let player play till max allowed is not exhaused --while loop
    #check 1: if player enters out of range, then throw error
    #check 2: if guessed number is either too low, too high or correct
        -- check if guessednumber< mysterynumber --> number is too low
        --check if guessnumber > mysterynumber --> number is too high
        -else correct number

'''


import random


def guessnumber():
    mystery_number = random.randint(1,100)
    wrong_guesses= 0
    max_wrong_guesses = 6

    while wrong_guesses < max_wrong_guesses: #if the wrong_guesses (0) < max_wrong_guesses (6) (to start with)
        guess_input = int(input("Guess a number between 1 and 100: "))

        if guess_input < mystery_number:
            print("Your number is too low, attempts left", wrong_guesses)
        elif guess_input > mystery_number:
            print("Your number is too high, attempts left:", wrong_guesses)
        else:
            print("You guessed the number")

        wrong_guesses +=1

        if wrong_guesses == max_wrong_guesses:
            print("You ran out of tries. The number was",mystery_number)

guessnumber()