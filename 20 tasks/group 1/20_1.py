def f(x,  p):
    if x >= 41 or p > 4 :
        return p == 4 and  x >= 41 
    if p % 2 == 1:
        return f(x + 1, p+1) or f(x + 10,  p + 1)
    else:
        return f(x + 1, p+1) and f(x + 10,  p + 1) 
   
for s in range(1, 40+1):
    if f(s, 1):
        print (s)