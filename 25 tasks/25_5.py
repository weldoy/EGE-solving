for i in range(111474, 10**10, 18579):
    number = str(i)
    if all([
        number[:2] == '54',
        number[3] == '1',
        number[5] == '3',
        number[-1] == '7'
    ]):
        print(i, i // 18579)
