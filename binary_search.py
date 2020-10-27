def binary_search(array, x, initial, final):
    middle = (initial + final) // 2

    if initial <= final:

        if x == array[middle]:
            return middle
        elif x < array[middle]:
            return binary_search(array, x, initial, middle-1)
        elif x > array[middle]:
            return binary_search(array, x, middle+1, final)

    else:
        print("there is no such value in this list!")
        return -1


def binary_search2(array, x):

    initial = 0
    final = len(array) - 1


    while initial <= final:

        middle = (initial + final) // 2
        if x == array[middle]:
            return middle
        elif x < array[middle]:
            final = middle - 1
        elif x > array[middle]:
            initial = middle + 1

    else:
        print("there is no such value in this list!")
        return -1





my_list = [i**2 for i in range(0, 10)]
print(my_list)
x_to_find = 2
print(binary_search(my_list, x_to_find, 0, len(my_list)-1))
print(binary_search2(my_list, x_to_find))