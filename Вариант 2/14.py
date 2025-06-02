for x in '0123456789ABCD':
    n = int(f'4B3{x}1C7', 14) + int(f'5{x}G83F7', 17)
    if n % 15 == 0:
        print(x, n // 15)
