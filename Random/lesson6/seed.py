from random import seed, randrange


for i in range(5):
    seed(i)
    table1 = ([randrange(3) for x in range(5)])
    table2 = ([randrange(3) for x in range(5)])

for cell in range(len(table1)):
    print(f"{table1[cell]}, {table2[cell]}")



print(f"{table1}, {table2}")


print([randrange(9,11,1) for i in range(5)])