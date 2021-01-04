from random import getrandbits

x = getrandbits(8)
print(x)
bits = []

for i in range(8):
    bits = [x % 2] + bits
    x = x // 2

print(bits)
