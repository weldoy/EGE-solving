for x in '0123456789ABCDEFG':
    n = int(f'5432{x}67', 17) + int(f'302{x}', 17)
    print(x)
    if n % 19 == 0:
        print(x, int(f'5432{x}67', 17) + int(f'302{x}', 17))
