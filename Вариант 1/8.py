from itertools import *


def f(n):
    evens = '02468ACEG'
    odds = '13579BDF'
    for i in range(len(n) - 2):
        if (n[i] in evens) and (n[i+1] in evens) and (n[i+2] in evens):
            return False
        if (n[i] in odds) and (n[i+1] in odds) and (n[i+2] in odds):
            return False
    return True


count = 0
for p in permutations('0123456789ABCDEFG', r=6):
    if f(p) and (p[0] != 0):
        count += 1
        # print(''.join(p))
print(count)
