for i in range(25, 10**7, 25):
    x = str(i)
    if x[0:2] == '89' and x[3:5] == '45' and x[-2:] == '75':
        print(i, i//25)
