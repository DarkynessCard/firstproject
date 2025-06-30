list = [1,2,3,4,5]
list1 = sum(list)
print(list1)


minimum = list1[0]
maximum = list1[0]

for num in list1:
    if num < minimum:
        minimum = num
    elif num > maximum:
        maximum = num

print(minimum)
print(maximum)
