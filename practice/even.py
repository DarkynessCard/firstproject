numlist = [10, 25, 5, 30, 15]
index = len(numlist) - 1
revlist = []

while index >= 0:
    if numlist[index] % 2 == 0:
        revlist.append(numlist[index])
    index -= 1

print(revlist)
