def diametr(cluster):
    maxr = 0
    for star1 in cluster:
        for star2 in cluster:
            maxr = max(d(star1, star2), maxr)
    return maxr
