from math import comb

print(comb(49, 6))
try:
    print(comb(-5, 6))
except ValueError:
    print("Error: must be non-negative")

try:
    print(comb(11.1, 6))
except TypeError:
    print("Error: must be an integer")
