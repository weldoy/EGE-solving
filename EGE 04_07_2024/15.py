for A in range(1, 500):
    flag = True
    for x in range(1, 500):
        for y in range(1, 500):
            f = (x + y <= 24) or (y <= x - 2) or (y >= A)
            if not f:
                flag = False
    if flag:
        print(A)
