from decimal import Decimal

D = Decimal
try:
    print(D(1) + 0.1)
except TypeError:
    print("you can't sum a Decimal with a float")

print(D(1) + D(0.1))
