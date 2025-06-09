n = '5' + 57 * '4'

while ('5454' in n) or ('554' in n) or ('444' in n):
    if '5454' in n:
        n = n.replace('5454', '2', 1)
    else:
        n = n.replace('554', '45', 1)
    n = n.replace('444', '54', 1)

print(n)
