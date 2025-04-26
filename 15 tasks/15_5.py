def f(x):
    return ((x % A != 0) and (132 <= x <= 150)) <= (x % 13 != 0)


for A in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(A)
