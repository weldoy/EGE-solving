n = 11*144**32 + 7144**27 - 13*144**19 + 2*12**29 - 249
a = ''

while n > 0:
    if n % 12 == 10:
        a += 'A'
    elif n % 12 == 11:
        a += 'B'
    else:
        a += str(n % 12)
    n //= 12

print(a.count('1') + a.count('2') + a.count('3') + a.count('4') +
      a.count('5') + a.count('6') + a.count('7') + a.count('8') +
      a.count('9') + a.count('A') + a.count('B'))
