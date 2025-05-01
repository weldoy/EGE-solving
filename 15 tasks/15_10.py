def f(x):
    return (((x|50) > 70) and ((x|17) <= 108)) <= (((x|108) > 17) and ((x|a) < 108))


for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(a)
