n = '12' * 80

while '121' in n or '22' in n:
    if '121' in n:
        n = n.replace('121', '2', 1)
    else:
        n = n.replace('22', '2', 1)
    print(n)

print('answer=', n)
