a, b, c = -1, -2, 1
lst = [-5458, -4516, 1119]


def func(x, y, z):
    if (x > 0) and (y < 0) and (z < 0):
        return True
    if (x < 0) and (y > 0) and (z < 0):
        return True
    if (x < 0) and (y < 0) and (z > 0):
        return True
    return False


if (a * b * c) <= (lst[1] * lst[2]):
    print(True)

print((a * b * c))
print((lst[1] * lst[2]))
