def d(star1, star2):
    return ((star2[0] - star1[0])**2 + (star2[1] - star1[1])**2) ** 0.5


def anticenter(cluster):
    max_len = 0
    dotanticenter = None
    for star1 in cluster:
        sum_len = 0
        for star2 in cluster:
            sum_len += d(star1, star2)
        if sum_len > max_len:
            max_len = sum_len
            dotanticenter = star1
    return dotanticenter


cluster_1 = []
cluster_2 = []
with open('27_1_А_iqpUwW7.txt') as f:
    f.readline()

    for line in f:
        x, y = [float(x) for x in line.replace(',', '.').split()]
        if y < 11:
            cluster_1.append((x, y))
        if y > 11:
            cluster_2.append((x, y))

    ac1 = anticenter(cluster_1)
    ac2 = anticenter(cluster_2)

    px = ac2[0]
    py = ac1[1]
    print(int(px * 10000 // 1))
    print(int(py * 10000 // 1))
