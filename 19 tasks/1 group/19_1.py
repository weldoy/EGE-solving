def f(x, p):
    if x >= 38 or p > 3:
        return p == 3 and x >= 38
    return f(x+1, p+1) or f(x+2, p+1) or f(x*2, p+1)

for s in range(1, 37+1):
    if f(s, 1):
        print(s)
        break
