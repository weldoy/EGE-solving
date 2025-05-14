def d(star1, star2):
    return ((star1[0] - star2[0]) ** 2 + (star1[1] - star2[1]) ** 2) ** .5


def center(cluster):
    min_length = 10**10
    cent_star = []
    for star1 in cluster:
        sum_length = 0
        for star2 in cluster:
            sum_length += d(star1, star2)
        if sum_length < min_length:
            min_length = sum_length
            cent_star = star1
    return cent_star


cluster_up = []
cluster_down = []

with open('27_A_19257.csv') as f:
    f.readline()
    for line in f:
        x, y = [float(x) for x in line.replace(',', '.').split()]
        if y > 5:
            cluster_up.append((x, y))
        else:
            cluster_down.append((x, y))

c1 = center(cluster_up)
c2 = center(cluster_down)
px = int(abs((c1[0] + c2[0]) / 2 * 10000) // 1)
py = int(abs((c1[1] + c2[1]) / 2 * 10000) // 1)

print(f'{px=} {py=}')
