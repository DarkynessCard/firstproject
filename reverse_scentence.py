def reverse_word(word):
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    print(reversed_word)
    return reversed_word

word = "racecar"
reversed_word = reverse_word(word)  # Call the function to get the reversed word

if reversed_word == word:
    print("True")
else:
    print("False")
