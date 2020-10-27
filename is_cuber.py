def is_cube(number):

    i = 0
    sq = i**3

    while sq < number:
        i += 1
        sq = i ** 3


    return sq == number, i





for i in range(1, 100+1):
    if is_cube(i)[0] == True:
        print(f"cube of num {is_cube(i)[1]} is  {i}")

