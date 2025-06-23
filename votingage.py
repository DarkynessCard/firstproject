#1. ask user for input N age
#2. if N > 17, print that you are eligible to vote
#3. if N < 17, print you are not eligible to vote

def checkvotingage(age, nationality):
    if int(age) > 17 and nationality =="US citizen":
        print("You are eligible to vote")
    elif int(age) > 17 and nationality !="US citizen":
        print("your age is right for vote but you hdon have right to vote")
    else:
        print("You are too young")



checkvotingage(5, "US itizen")
