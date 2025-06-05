def d(star1, star2):
    return ((star1[0] - star2[0])**2 + (star1[1] - star2[1])**2)**0.5


def center(cluster):
    min_len = 10**10
    cent_star = None
    for star1 in cluster:
        sum_len = 0
        for star2 in cluster:
            sum_len += d(star1, star2)
        if sum_len < min_len:
            min_len = sum_len
            cent_star = star1
    return cent_star


def anticenter(cluster):
    maxlen = 0
    cent_star = None
    for star1 in cluster:
        sum_len = 0
        for star2 in cluster:
            sum_len += d(star1, star2)
        if sum_len > maxlen:
            maxlen = sum_len
            cent_star = star1
    return cent_star


cluster1 = []
cluster2 = []
with open('27A_22625.txt') as f:
    for line in f:
        x, y = [float(x) for x in line.replace(',', '.').split()]
        if y > 15:
            cluster1.append((x, y))
        else:
            cluster2.append((x, y))

c1 = center(cluster1)
c2 = center(cluster2)
ac1 = anticenter(cluster1)
ac2 = anticenter(cluster2)

px = (c1[0] + c2[0]) / 2
sy = (ac1[1] + ac2[1]) / 2

print(int(abs(px*10000)//1), int(abs(sy*10000)//1))
