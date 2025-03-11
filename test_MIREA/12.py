n = '123' * 40

while '12' in n or '333' in n:
    if '12' in n:
        n = n.replace('12', '3', 1)
    else:
        n = n.replace('333', '3', 1)

print(n)
