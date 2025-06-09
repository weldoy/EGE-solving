import itertools

odds = '13579'


def duck(x):
    k = 0
    for x in range(len(i) - 1):
        a = (i[k] + i[k + 1])
        if a in ('1X', 'X1', 'X3', '3X', 'X5', '5X', 'X7', '7X', 'X9', '9X'):
            return False
        k += 1
    return True


count = 0
for i in itertools.product('0123456789ABCD', repeat=5):
    i = (''.join(i)).replace('A', 'X')
    i = (''.join(i)).replace('B', 'X')
    i = (''.join(i)).replace('C', 'X')
    i = (''.join(i)).replace('D', 'X')
    if i[0] != '0':
        if duck(i):
            count += 1
            print(i)

print(count)
