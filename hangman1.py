import random  # Get a random word from the list

def hangman(word_list):
    word = random.choice(word_list).lower() #Pick a random word
    guessed_letters = [] #Store the letters guessed
    display_word = ["_"] * len(word) #Hide the wrd with underscores
    wrong_guesses= 0
    max_wrong_guesses = 6

    print("Welcome to Hangman!")
    print("Guess the word")
    print(" ".join(display_word))  # show underscores seperated by spaces

    guess_letter_logic(display_word, guessed_letters, max_wrong_guesses, word, wrong_guesses)

    display(display_word, word)


def display(display_word, word):
    if "_" not in display_word:
        print("Great job! You guessed the word:", word)
    else:
        print("Game over! The word was:", word)


def guess_letter_logic(display_word, guessed_letters, max_wrong_guesses, word, wrong_guesses):
    while wrong_guesses < max_wrong_guesses and "_" in display_word:
        guess = input("Enter a letter: ").lower()  # Ask player to guess a letter

        # Check if guess is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter (A-Z).")
            continue

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Check if guess is in the word
        if guess in word:
            print("Good guess!")
            # Reveal all positions of the guessed letter
            for i in range(len(word)):
                if word[i] == guess:
                    display_word[i] = guess

        else:
            print("Wrong guess")
            wrong_guesses += 1
            print("Guesses left:", max_wrong_guesses - wrong_guesses)

        # Show current progress
        print("\nWord:", " ".join(display_word))
        print()


#List of words to play with
word_list = ["python", "developer", "hangman", "robot", "coding"]
hangman(word_list)

