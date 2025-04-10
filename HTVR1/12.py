n = '1' * 81

while '111' in n or '88888' in n:
    if '111' in n:
        n = n.replace('111', '88', 1)
    if '88888' in n:
        n = n.replace('88888', '8', 1)

print(n)
