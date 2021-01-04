from copy import copy, deepcopy

ml = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ml2 = ml

ml2[0][0] = 10
print(ml)
print(ml2)
print("")

ml = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ml3 = copy(ml)
ml3[1] = [0]
ml3[0][0] = 0
print(ml)
print(ml3)
print("")

ml = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ml3 = deepcopy(ml)
ml3[1] = [0]
ml3[0][0] = 0
print(ml)
print(ml3)
