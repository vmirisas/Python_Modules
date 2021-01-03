from random import choice, choices, shuffle, sample

my_list = list(range(5))
print(f"Random choice: {choice(my_list)}")
print(f"3 Random choices: {choices(my_list, k=3)}")
print(f"5 Weighted choices: {choices(my_list, [1, 100, 10, 1, 1], k=10)}")
print(f"5 Cum.W. choices: {choices(my_list, cum_weights=[1, 101, 111, 112, 113], k=10)}")

my_list2 = [1, 2, 3, 4, 5, 6, 5, 7, 7, 7, 9]
print(my_list2)
shuffle(my_list2)
print(my_list2)


print(sample(my_list2, 5))