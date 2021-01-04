from decimal import Decimal

D = Decimal
fpacc = Decimal(10) ** -2

a = D("0.43")
b = D("12.93")
print(a * b)
print((a * b).quantize(fpacc))
