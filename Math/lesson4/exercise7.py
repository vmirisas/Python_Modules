from math import gamma, factorial

for x in range(2, 10+1):
    print(f"gamma({x})={gamma(x)}, factorial({x-1})={factorial(x-1)})")