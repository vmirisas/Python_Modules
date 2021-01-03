from random import seed, randrange

seed()
list1 = [randrange(100, 201) for x in range(10)]
list2 = [randrange(0, 10, 2) for x in range(10)]
list3 = [randrange(102, 201, 3) for x in range(10)]
list4 = [divmod(list3[x], 3) for x in range(10)]
list5 = [(list3[x] % 3) for x in range(10)]
print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
