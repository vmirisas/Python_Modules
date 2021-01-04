from decimal import Decimal

D = Decimal
print(D(1))
print(D('3.14'))
print(D(3.14))
print(D(3.140000000000000000000000000435345698346759137846591675))
print(D((1, (1, 4, 1, 5), -1)))
print(D("NaN"))
print(D("infinity"))
print(D("-infinity"))
