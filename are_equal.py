
def are_equal(a, b):
    if a == b:
        print("Equal")
    else:
        print("Not Equal")

are_equal(4, 5)

def fahrenheit_to_celsius(fahrenheit):
  celsius = fahrenheit*9/5 + 32
  print(celsius)

fahrenheit_to_celsius(0)

def last_letter1(input):

  if input:
    last_letter = input[-1]
    print(last_letter)
  else:
    print("The string is empty.")


last_letter1("hello")

def first_letter1(word, letter):

    if letter in word[0]:
        print("Yes")
    else:
        print("No")

first_letter1("hello", "h")

def divisible(num1, num2):
  if num1 % num2 == 0:
    print("Is divisible")
  else:
    print("Not divisible")

divisible(5, 5)
