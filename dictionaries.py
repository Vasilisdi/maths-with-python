from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now)

numbers = {}  #so as to define a dictionary
#note that for sets despire the fact we use {}
#we define the sets using set()

for i in range(1,6+1):
    numbers[i] = 0

for _ in range(100000):
    num = randrange(1, 6+1)
    numbers[num] += 1

print(numbers)

other = {}
other = {
    "giannis" : 5,
    "pol" : 2,
    "anthi" : "gunaika"

}

other["kavani"]= "antras"

print(other)


#another proj
string = "I m writing this test for the purpose of gaining some intuition into the dictionaries of python"
my_list = list(string)

dictionary = {}

for char in my_list:
    if char not in dictionary:
        dictionary[char] = 1
    else:
        dictionary[char] += 1

print(dictionary)
print(dictionary.values())
print(list(dictionary.values()))
print(max(list(dictionary.values())))

max_v = max(list(dictionary.values()))

for key, value in dictionary.items():   #SOS - paei 1-1 , -2-2 , 3-3 , 4-4
    print( str(key) + " " + str(value) + " " + str(max_v))
    if value == max_v:
        if key == " ":
            print(f"my key: blank and the value: {value}  respectively")
        else:
            print("my key: " + key + "    and my value: " + str(value))


print("my dictionary= " + str(dictionary))
print(dictionary.items())
print(dictionary.values())
print(dictionary.keys())
print(list(dictionary.values()))


#a simple way to create a dictionary

string = "jjafa alksfjask a lskjd asllka jkdlas jalksd jal dasj klajs sakljdsalk aaaa2"

letters = set(string)   #facilitates the process above
new_dictionary = {letter: 0 for letter in letters} #very good


for char in string:
    new_dictionary[char] += 1

for key in sorted(new_dictionary.keys()):
    print(key + " : " + str(new_dictionary[key]))

print(string.find("2"))  # can find sth
print(string.index("2"))

pos = -1
lpos = string.rfind("a") # the last a
# print(lpos)



# finding the pos of the letter a

while pos != lpos:
    pos = string.find("a", pos+1)
    print(pos, end=" ")

print("\n")
print(" %f " %(1/3))
print(" %.2f %.4f " %(1/3 , 1/8))
