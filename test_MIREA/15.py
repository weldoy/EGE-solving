for A in range(1, 300):
    flag = True
    for x in range(1, 300):
        for y in range(1, 300):
            f = ((x*x <= A) <= (x <= 7)) and ((y < 4) <= (y*y <= A))
            if not f:
                flag = False
    if flag:
        print(A)
