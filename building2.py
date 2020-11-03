class Flat:
    def __init__(self):
        self.people = 0

class  Storey:
    def __init__(self, number_flats):
        self.flats = [Flat() for _ in range(number_flats)]

class Building:
    def  __init__(self, number_storeys, number_flats):
        self.storeys = [Storey(number_flats) for _ in range(number_storeys)]


def add_people(storey, flat, people):
    my_building.storeys[storey].flats[flat].people += people


def print_people():
    for i in range(len(my_building.storeys)):
        for j in range(len(my_building.storeys[i].flats)):
            print(f" Storey { i +1 } in flat { j + 1} contains {my_building.storeys[i].flats[j].people} people")


i = 2 #storeys
j = 3 #flats per storey
k = 5 #num of people
my_building = Building(i, j)


# insert the residents
add_people(1, 0, 5)
add_people(0, 1, 5)
add_people(1, 2, 5)


print_people()