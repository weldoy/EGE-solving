for x in '0123456789ABCDEFGHIJKLM': 
    # for x in range(23) - писать нельзя, тк нет 10, 11 и тд...
    # Только 0123456789 и алфавит...
    x1 = int(f'11353{x}12', 23)
    x2 = int(f'135{x}21', 23)
    if (x1 + x2) % 22 == 0:
        print(x, (x1 + x2) // 22)