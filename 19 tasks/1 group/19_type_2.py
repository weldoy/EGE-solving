def f(x,  p):
    if x >= 65 or p > 3 :
        return (p == 3 and x >= 65) 
    
    if p % 2==0:
        return f(x + 1, p+1) or f(x +2,  p + 1) or f(x * 3,  p + 1)
    else:
        return f(x + 1, p+1) and f(x +2,  p + 1) and f(x * 3,  p + 1)
    
for s in range(1, 64+1):
    if f(s, 1):
        print (s)
        