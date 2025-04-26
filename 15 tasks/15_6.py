def f(x):
    return (((x | 42) > 64) and ((x | 34) <= 102)) <= (not((x | A) < 70))


for A in range(0, 1000):
    if all(f(x) for x in range(0, 1000)):
        print(A)
        break
