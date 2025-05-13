def f(x, y, z):
    return (x <= (not z)) and ((not y) <= x)


t = (
    (0, 1, 0, False),
    (1, 1, 0, True)
)

print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(x, y, z, f(x, y, z))

# if len(set(t)) == len(t):
#     if all(f(t) == m[-1] for m in t):
