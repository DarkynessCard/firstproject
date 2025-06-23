
'''
square = lambda a,b: a+b
print(square(3,3))

list1 = [1,2,3,4,5,6,7]
'''

'''algo:
get word from user
run loop checking characters in word
if the character is lowercase, append it to newlist and make it upercase
else: append to newlist and make it lowercase'''


def changecase(str1):

    result = ""

    for char in str1:
        if char.islower():
            result += char.upper()
        else:
            result +=char.lower()
    print(result)

#changecase("HELo")


'''ask user for a scentence
if there are any digit in the scentence then add the word it to the list'''
'''have empty list'''



def number1(sentence):
    result = ""
    word = sentence.split()

    for char in word:
        if not char.isalpha():
            result+= char+" "
    print(result)

number1("You are amaz1ng  kid")



