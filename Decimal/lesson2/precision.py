from decimal import getcontext, Decimal
D = Decimal

getcontext().prec = 3
a = D("0.4391")
b = D("12.939")
print(a, b, b/a)

print(getcontext())