n = '213' * 50

while '31' in n or '32' in n:
    if '32' in n:
        n = n.replace('32', '3', 1)
    else:
        n = n.replace('31', '11', 1)

print(n.count('1'))
