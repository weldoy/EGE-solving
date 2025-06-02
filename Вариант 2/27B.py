def d(star1, star2):
    return ((star1[0] + star2[0])**2 + (star1[1] + star2[1])**2)**.5


def center(cluster):
    min_length = 10**10
    cent_star = None
    for star1 in cluster:
        sum_length = 0
        for star2 in cluster:
            sum_length += d(star1, star2)
        if sum_length < min_length:
            min_length = sum_length
            cent_star = star1
    return cent_star


def density(cluster):
    return len(cluster) / 16


cluster1 = []
cluster2 = []
cluster3 = []
cluster4 = []
cluster5 = []
with open('27B_22623.txt') as f:
    f.readline()
    for line in f:
        x, y = [float(x) for x in line.replace(',', '.').split()]
        if x < 0:
            cluster1.append((x, y))
        if x > 0 > y:
            cluster2.append((x, y))
        if 10 < x < 20 and 15 < y < 22:
            cluster3.append((x, y))
        if 10 < x < 20 and y > 22:
            cluster4.append((x, y))
        else:
            cluster5.append((x, y))


c1 = center(cluster1)
c2 = center(cluster2)
c3 = center(cluster3)
c4 = center(cluster4)
c5 = center(cluster5)

p1 = density(cluster1)
p2 = density(cluster2)
p3 = density(cluster3)
p4 = density(cluster4)
p5 = density(cluster5)

ps = (p1 + p2 + p3 + p4 + p5) / 5
sp = d(c4, c5)
print(int(ps*1000 // 1), int(sp*1000 // 1))
