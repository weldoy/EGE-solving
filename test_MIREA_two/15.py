for A in range(1, 100):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not ((3*x + y < A) or (x < y) or (16 <= x)):
                flag = False
    if flag:
        print(A)

