def f(x, y):
    return (3*x + y > A) and (y < x) and (x < 30)


for A in range(0, 1000):
    if all(f(x, y) == 0 for x in range(0, 300) for y in range(0, 300)):
        print(A)
        break
