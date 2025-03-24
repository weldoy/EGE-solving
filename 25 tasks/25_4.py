for i in range(451, 10**9, 451):
    number = str(i)
    if all([
        number[:2] == '10',
        number[3:6] == '451',
        number[-1] == '3'
    ]):
        print(i, i // 451)
