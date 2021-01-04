from random import getstate, setstate, randint

state = None

for i in range(10):
    print(i, randint(1, 10))
    if i == 5:
        state = getstate()
print("=" * 10)
setstate(state)
for i in range(6, 10):
    print(i, randint(1, 10))
