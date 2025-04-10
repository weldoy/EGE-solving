for i in range(10**7, 0, -1):
    n = str(i)
    if all([
        n[0:2] == '89',
        n[3:5] == '45',
        n[-2:] == '75'
    ]):
        print(i, i // 25)
