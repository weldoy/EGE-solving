def f(x, p):
    if x >= 68 or p > 3:
        return p == 3 and x > 68
    return f(x+1, p+1) or f(x+4, p+1) or f(x*5, p+1)

for s in range(1, 67+1):
    if f(s, 1):
        print(s)
        break