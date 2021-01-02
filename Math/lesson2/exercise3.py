from math import e


def f(x):
    return 1 / (1 + pow(e, -x))


for x in range(10):
    print(f"f({x}) = {f(x)}")
