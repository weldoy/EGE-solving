n = '3' * 234

while ('33333' in n) or ('1111' in n):
    if '33333' in n:
        n = n.replace('33333', '111', 1)
    else:
        n = n.replace('111', '33', 1)

print(n)
print(3**5)
