from math import pow, exp, sqrt, isqrt, frexp, ldexp, expm1, e


print(f"pow(3,2) = {pow(3,2)}")#returns float
print(f"3**2 = {3**2}")# returns integer

print(f"exp(2) = {exp(2)}")

print(f"sqrt(9) = {sqrt(9)}")
print(f"sqrt(2) = {sqrt(2)}")

print(f"isqrt(9) = {isqrt(9)}")# returns the integer part
print(f"isqrt(2) = {isqrt(2)}")# returns the integer part

print(f"expm1(3) = {expm1(3)}")# returns the value of: e ^ x - 1
print(f"expm1(0) = {expm1(0)}")

print(f"ldexp(0) = {ldexp(2,1)}")# returns the value of: x * 2 ^ y
print(f"ldexp(0) = {ldexp(1,0)}")# returns the value of: x * 2 ^ y

print(f"frexp(3) = {frexp(3)}")
x1 = 0.75 * pow(2, e)
x2 = frexp(x1)
print(x1, x2)