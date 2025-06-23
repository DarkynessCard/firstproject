'''a function is a block of code that does specific functionality
built-in functions ( print, append, str, etc)
user-defined functions (types - none, return type, int, string, float)
lambda functions(key pair, used when you think you do not need to re-use)
'''

#Find the sum of all odd numbers in given list


def sumodd():
    list = (1, 2, 3, 4, 5, 6, 7, 8)
    sum = 0
    for i in list:
        if i % 2 != 0:
            sum += i
    print(sum)


sumodd()
