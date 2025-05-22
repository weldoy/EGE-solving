from fnmatch import fnmatch


def divisors(x):
    b = set()
    for i in range(1, int(x**.5)+1):
        if x % i == 0:
            if i % 2 == 0:
                b.add(i)
            if (x//i) % 2 == 0:
                b.add(x//i)
    return sorted(b)


count = 0
for i in range(65000 + 1, 10**10):
    if fnmatch(str(i), '6*97*5?'):
        if len(divisors(i)) >= 4:
            count += 1
            if count <= 7:
                print(i, sum(divisors(i)))
            else:
                break
