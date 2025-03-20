for x in range(700001, 710000):
    sq = int(x**0.5)
    d = set()
    for i in range(2, sq+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    if d:
        M = max(d) + min(d)
        if M % 10 == 8:
            print(x, M)
