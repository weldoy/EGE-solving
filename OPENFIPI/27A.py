def d(star1, star2):
    return ((star2[0] - star1[0]) ** 2 + (star2[1] - star1[1]) ** 2) ** .5


def center(cluster):
    cent_star = None
    min_length = 10**10
    for star1 in cluster:
        sum_length = 0
        for star2 in cluster:
            sum_length += d(star1, star2)
        if sum_length < min_length:
            min_length = sum_length
            cent_star = star1
    return cent_star


clusterUP = []
clusterDOWN = []
with open('27_A_21911.txt') as file:
    file.readline()

    for line in file:
        x, y = [float(n) for n in line.replace(',', '.').split()]
        if y > 2:
            clusterUP.append((x, y))
        else:
            clusterDOWN.append((x, y))
    c1 = center(clusterUP)
    c2 = center(clusterDOWN)
print(f'{c1=} {c2=}')
px = int(((c1[0] + c2[0]) / 2 * 10000) // 1)
py = int(((c1[1] + c2[1]) / 2 * 10000) // 1)

print(px, py)
