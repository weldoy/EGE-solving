for A in range(1, 300):
    flag = True
    for x in range(1, 300):
        for y in range(1, 300):
            if not((5 < y) or (x > 32) or (x + 2*y < A)):
                flag = False
    if flag:
        print(A)
        