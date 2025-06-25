numbers = [1, 2, 3, 2, 5]

checked = []

for i in range(len(numbers)):
    if numbers[i] in checked:
        continue
#count occurences
    count = 0
    for p in range(len(numbers)):
        if numbers[p] == numbers[i]:
            count += 1

    print(f"{numbers[i]} occurs {count} time(s)")

    checked.append(numbers[i])


