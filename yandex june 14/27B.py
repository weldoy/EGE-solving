def d(star1, star2):
    return ((star1[0] - star2[0]) ** 2 + (star1[1] - star2[1]) ** 2) ** 0.5


def center(cluter):
    cent_star = None
    minlen = 10**10
    for star1 in cluter:
        sumlen = 0
        for star2 in cluter:
            sumlen += d(star1, star2)
        if sumlen < minlen:
            minlen = sumlen
            cent_star = star1
    return cent_star


def radius(cluster):
    cent_star = center(cluster)
    maxlen = 0
    for star in cluster:
        length = d(cent_star, star)
        if length > maxlen:
            maxlen = length
    return maxlen


cluster1 = []
cluster2 = []
cluster3 = []
cluster4 = []
cluster5 = []
with open('27_Б.txt') as f:
    for line in f:
        x, y = [float(x) for x in line.replace(',', '.').split()]
        if y > 15:
            cluster1.append((x, y))
        if 7 < y < 15 and x < 10:
            cluster2.append((x, y))
        if x > 10 and 7 < y < 13 :
            cluster3.append((x, y))
        if x < 7 and y < 6:
            cluster4.append((x, y))
        if x > 15 and y < 7:
            cluster5.append((x, y))


r1 = radius(cluster1)
r2 = radius(cluster2)
r3 = radius(cluster3)
r4 = radius(cluster4)
r5 = radius(cluster5)

print(int(min(r1, r2, r3, r4, r5) * 10000 // 1))
print(int(max(r1, r2, r3, r4, r5) * 10000 // 1))
