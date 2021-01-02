from math import frexp

for x in range(100+1):
    print(f"{x} {frexp(x)}")