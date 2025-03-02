def f(x, y, p):
    if x + y >= 82 or p > 3:
        return p == 3 and x + y >= 82
    if p % 2 == 1:
        return f(x+1, y, p+1) or f(x*4, y, p+1) or f(x, y+1, p+1) or f(x, y*4, p+1)
    else:
        return f(x+1, y, p+1) and f(x*4, y, p+1) and f(x, y+1, p+1) and f(x, y*4, p+1)


for s in range(1, 77+1):
    if f(4, s, 1):
        print(s)
