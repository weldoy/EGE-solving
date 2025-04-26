def treug(n, m, k):
    return True if ((n > (m+k)) or (m > (n+k)) or (k > (m+n))) else False


def maximus(a, b):
    return a if a > b else b


for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not(not((treug(x, 12, 20) == (not(maximus(x, 5) > 28))) and treug(x, A, 3))):
            flag = False
    if flag:
        print(A)
