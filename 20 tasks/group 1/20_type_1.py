def f(x,  p):
    if x >= 68 or p > 4 :
        return p == 4 and  x >= 68 
    if p % 2 == 1:
        return f(x + 1, p+1) or f(x + 4,  p + 1) or f(x * 5,  p + 1)
    else:
        return f(x + 1, p+1) and f(x + 4,  p + 1) and f(x * 5,  p + 1) 
   
for s in range(1, 67+1):
    if f(s, 1):
        print (s)