def d(star1, star2):
    return ((star2[0] - star1[0])**2 + (star2[1] - star1[1])**2) ** .5


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


cluster1 = []
cluster2 = []
cluster3 = []
with open('27B.csv') as file:
    for line in file:
        x, y = [float(x) for x in line.replace(',', '.').split()]
        if x < 0:
            cluster1.append((x, y))
        if (x > 0) and (y < 7):
            cluster2.append((x, y))
        if (x > 0) and (y > 7):
            cluster3.append((x, y))

c1 = center(cluster1)
c2 = center(cluster2)
c3 = center(cluster3)
px = int(abs((c1[0] + c2[0] + c3[0]) / 3 * 10000) // 1)
py = int(abs((c1[1] + c2[1] + c3[1]) / 3 * 10000) // 1)

print(px, py)
