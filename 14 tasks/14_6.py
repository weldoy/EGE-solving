for x in range(1, 5556):
    n = 5**150 + 5**135 - x
    a = ''
    while n > 0:
        a += str(n % 5)
        n //= 5
    if a.count('4') == 134:
        print(f'{x=}\n {a.count('4')=}')
