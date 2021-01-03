from random import randrange, shuffle


def print_seq_cities(cities, seq):
    for i in range(len(cities)):
        print(cities[seq[i]], end=" ")


cities = ["A", "B", "C", "D", "E"]

distances = [[randrange(100) for j in range(5)] for i in range(5)]


ml = list(range(5))

for i in range(2):
    shuffle(ml)
    print_seq_cities(cities, ml)
    distance = 0
    for x in range(5 - 1):
        distance += distances[ml[i]][ml[i + 1]]
    print(" Total distance: " + str(distance))
