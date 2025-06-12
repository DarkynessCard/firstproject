#Function to run the hangman game

import random

def hangman():
    #Step 1: List of words to choose from
    word_list = ["python", "developer", "hangman", "programming", "challenge"]

        #step 2: randomly choose a word from the list
    word = random.choice(word_list).lower()

    #step 3: Store guessed letters and initial game state
    guessed_letters = set() #Letters guessed so far
    display_word = ["_" for _ in word] #The word with unguessed letters hidden
    max_wrong_guesses = 6 #Number of allowed wrong guesses
    wrong_guesses = 0 # Counter for wrong guesses

    #Step 4: Show the initial blank word
    print("Welcome to Hangman!")
    print("Guess the word")
    print(" ".join(display_word)) #show underscores seperated by spaces

    #Step 5: Start the game loop
    while wrong_guesses < max_wrong_guesses and "_" in display_word:
        guess = input("Enter a letter: ").lower() #Ask player to guess a letter

        #Step 6: Validate inout
        if not guess.isalpha() or len(guess) !=1:
            print("! Please enter a single alphabetic character.")
            continue

        #Step 7: Check if the letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        #Step 8: Add guess to guessed letters
        guessed_letters.add(guess)

        #Step 9: Check if guess is in the word
        if guess in word:
            #Reveal all occurrences of the letter in the display
            for i, char in enumerate(word):
                if char == guess:
                    display_word[i] = guess
            print("Good guess!")
        else:
            #Wrong guess: increment the counter
            wrong_guesses +=1
            print(f"Wrong Guess! You have {max_wrong_guesses - wrong_guesses} guesses left.")

        #Step 10: Show current game state
        print("\nWord: " + " ".join(display_word)) # Sorted guessed letters
        print() # Add an empty line for redobility

    #Step 11: End of game - check win or loss
    if "_" not in display_word:
        print(f"Congratulations! You guessed the word: '{word}' ")
    else:
        print(f"Game over! The word was: '{word}'")
hangman()




