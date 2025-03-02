def f(x, y, A):
    return (x < A) or (y < A) or (x + 2 * y > 50)

for A in range(100):
    flag = True
    for x in range(100):
        for y in range(100):
            if not f(x, y, A):
                flag = False
    if flag == True:
        print(A)
