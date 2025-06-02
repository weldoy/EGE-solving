for A in range(0, 100):
    flag = True
    for x in range(0, 100):
        f = (((x&117) != 0) and ((x&91) == 0)) <= ((x&A) != 0)
        if not f:
            flag = False

    if flag:
        print(A)
