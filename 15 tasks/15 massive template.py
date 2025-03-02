p = {1, 3, 7}
q = {1, 2, 4, 5, 6}

def f(x, a):
    return ((x not in a) <= (x not in p)) or ((x not in q) and (x in p))


a = set() # МАКС - a = set(range(1, 1000))

for x in range(1, 1000):
    if not f(x, a):
        a.add(x) # МАКС a.remove(x)

print(sorted(a)) # МАКС max(a)
