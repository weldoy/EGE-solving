for i in range(2024, 10**10, 2024):
    number = str(i)
    if all([
        number[0] == '1',
        number[-1] == '4',
        number[2:6] == '2157'
    ]):
        print(i, i // 2024)
