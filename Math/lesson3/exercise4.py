from math import modf, fmod, pi

x = modf(pi)
print(x[0])
print(x[1])
print(x)
print(type(modf(pi)))

# returns the remainder of x/y
print(fmod(20, 4))
print(fmod(20, 3))
print(fmod(15, 6))
print(fmod(-10, 3))
try:
    print(fmod(0, 0))
except ValueError:
    print("Throws Value Error")
