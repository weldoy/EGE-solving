for A in range(1, 300):
    flag = True
    for x in range(1, 300):
        if not(x % A == 0 or ((60 <= x <= 80) <= x % 22 != 0)):
            flag = False

    if flag:
        print(A)
