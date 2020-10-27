def is_square(number):

    i = 0
    sq = i**2

    while sq < number:
        i += 1
        sq = i ** 2

    return sq == number

print(is_square(63))