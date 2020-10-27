def digits_adjacent_to_isolate(number):


    num_of_digits = 0
    digits_list = []
    length = len( str(number) )
    dic = {}


    for i in range(1, length + 1 ):

        num_of_digits += 1
        if digits_list == []:
            digits_list.append(number % 10)                                   # modulus
        else:
            digits_list.append((number // (10 ** (num_of_digits - 1)) % 10))  # floor division

        dic[num_of_digits] = digits_list[num_of_digits - 1]




    return digits_list , dic


num = int(input("give the number:  "))

for i in range(1, len(digits_adjacent_to_isolate(num)[0])+1):
    print(f" digit {list(digits_adjacent_to_isolate(num)[1].keys())[i-1]} is "
          f"  {list(digits_adjacent_to_isolate(num)[1].values())[i-1]} ")

