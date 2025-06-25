def get_min_max(numbers):

    minimum = numbers[0]
    maximum = numbers[0]

    for num in numbers:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num

    print(minimum)
    print(maximum)

get_min_max([1, 2, 3, 4, 5, 6, 7])
