from math import log, log10, log2, e

print(log(e))

for x in [1, 10, 100, 1000]:
    print(f"===== x = {x} =====")
    print(f"log({x}) = {log(x)}")
    print(f"log10({x}) = {log10(x)}")
    print(f"log({x}) = {log2(x)}")
    print("")
