'''
list = ["game","python","script"]
for word in list
iterate over the list
random.sample(word)
'''
import random

def get_random_word():
    words = ['python','developer','hangman','jumble','learning','project','school','keyboard']
    return random.choice(words)

def jumble_word(word):
    return ''.join(random.sample(word,len(word)))

def play_game():
    print("Welcome to the Word Jumble Game!")
    score = 0
    play = True

    while play:
        original_word = get_random_word()
        jumbled = jumble_word(original_word)

        print(f"\nJumbled word: {jumbled}")
        guess = input("Your guess: ").lower()

        if guess == original_word:
            print("Correct! Well done.")
            score+=1
        else:
            print(f"Wrong! The correct word was: {original_word}")

        again = input("Do you want to play again? (yes/no):").lower()
        if again != 'yes':
            play = False

    print(f"\nThanks for playing! Your final score is: {score}")

if __name__ == "__main__":
    play_game()