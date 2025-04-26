def treug(n, m, k):
    if ((n+m) > k) and ((n+k) > m) and ((k+m) > n):
        return True
    return False


def f(x):
    return not((treug(x, 12, 20) == (max(x, 5) <= 28)) and treug(x, A, 3))


for A in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(A)
