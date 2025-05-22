def d(star1, star2):
    return ((star2[0] - star1[0])**2 + (star2[1] - star1[1])**2) ** .5


def diam(cluster):
    min_len = 10**10
    diametr = None
    for star1 in cluster:
        diams = []
        for star2 in cluster:
            diams.append(d(star1, star2))
        if sum(diams) < min_len:
            min_len = min(diams)
            diametr = min_len
    return diametr


cluster_up1 = []
cluster_up2 = []
cluster_down1 = []
cluster_down2 = []
with open('27A-1.txt') as f:
    f.readline()
    for line in f:
        x, y = [float(x) for x in line.replace(',', '.').split()]
        if x < 2 and y < 0:
            cluster_down1.append((x, y))
        if x < 2 and y > 0:
            cluster_up1.append((x, y))
        if x > 2 > y:
            cluster_down2.append((x, y))
        if x > 2 and y > 2:
            cluster_up2.append((x, y))

d1 = diam(cluster_up1)
d2 = diam(cluster_up2)
d3 = diam(cluster_down1)
d4 = diam(cluster_down2)

px = int(d1)
