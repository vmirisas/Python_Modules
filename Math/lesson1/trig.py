from math import pi, sin, cos, tan

for i in range(4):
    v = i * pi / 2
    print(f"===== I = {i} =====")
    print(f"sin({i}*PI/2) = {sin(v)}")
    print(f"cos({i}*PI/2) = {cos(v)}")
    print(f"tan({i}*PI/2) = {tan(v)}")
    print("")

    print(f"I = {i} in floats")
    print(f"sin({i}*PI/2) = {sin(v):.2f}")
    print(f"cos({i}*PI/2) = {cos(v):.2f}")
    print(f"tan({i}*PI/2) = {tan(v):.2f}")
    print("")
