d1, d2, c1, c2 = 17, 58, 29, 80
d = [i/10 for i in range (d1*10, d2*10+1)]
c = [i/10 for i in range (c1*10, c2*10+1)]

a = set()

f = [i/10 for i in range (0, 1000)]

for x in f:
    if not((x in d)<=(((not(x in c)) and (not(x in a)))<=(not(x in d)))):
        a.add(x)

t = sorted(a)

print(*t)

# answer = максимальное - минимальное
# ответ = 28.9 tasks = 29 - 17 = 12
    
