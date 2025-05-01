n = '3' * 92

while '999' in n or '333' in n:
    if '999' in n:
        n = n.replace('999', '3', 1)
    if '333' in n:
        n = n.replace('333', '9 tasks', 1)

print(n)