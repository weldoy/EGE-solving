def f(x, A):
    x1 = x % A != 0
    x2 = x % 28 == 0
    x3 = x % 49 != 0
    return x1 <= (x2 <= x3)

for A in range(1, 300):
    flag = True
    for x in range(1, 300):
        if not f(x, A):
            flag = False
    if flag:
        print(A)
