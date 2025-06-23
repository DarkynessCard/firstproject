#Function to run the hangman game
'''
Need opening hook



first, we have a wordlist which contains the words
since we imported random, we can use random.choice to pick a random word from our wordlist
then for our display word, we print out underscores. We find the length of the random word and print out the same length of underscores.
we have our variables called max_wrong_guesses which we can set to determine how many attempts the user has
I set the max_wrong_guesses to 6
we also have a counter called wrong_guesses which is set to 0 at the start
Now we introduce the user to the game
After that, we have a loop that checks if the amount of wrong_guesses is less than the amount of max_wrong_guesses
and that there are still blank spaces in the word:
we can ask the user to enter a letter
now we check if the input is a letter and it is less than 2
if both of those are satistfied, we now add the guess to the guessed_letters so the user will know if he used the letter before
we loop through the random word and check if the letter is in the word
now we print("Good guess")
if your guess is not in the random word, we print Wrong Guess. Then add 1 to the counter of wrong_guesses
Now we show the current game state
The loop will let you have another guess until you reach max_wrong_guesses
We check if there are still blank spaces in the random word, if there aren't any in the random word, you win
if there is, you lose. Now we call the function back.

'''
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




