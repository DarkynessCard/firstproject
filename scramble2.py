'''
list = ["game","python","script"]
for word in list
iterate over the list
random.sample(word)

From 1 player to scramble then ask another player to unscramble
if player2 guesses correct then get 1 score with every correct guess
if wrong then subtract 1 from score but let player to play again.
'''

'''alg: import random to randomize word
'''
import random
def getwordfromuser():
    word = input("Enter a word to scramble \n")
    return word

def jumble_word(word):
    return ''.join(random.sample(word,len(word)))

def play_game():
    print("Welcome to the Word Jumble Game!")
    score = 0
    play = True

    while play:
        original_word = getwordfromuser()
        jumbled = jumble_word(original_word)

        print(f"\nJumbled word: {jumbled}")
        guess = input("Your guess: ").lower()

        if guess == original_word:
            print(f"Correct! Well done.")
            score+=1
            print(f"Your score is {score}")
        else:
            print(f"Wrong! The correct word was: {original_word}. Your score is {score}")
            if score > 0:
                score-=1

        again = input("Do you want to play again? (yes/no):").lower()
        if again != 'yes':
            play = False

    print(f"\nThanks for playing! Your final score is: {score}")

if __name__ == "__main__":
    play_game()