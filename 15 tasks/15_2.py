# Треугольник существует только тогда, когда сумма двух его сторон больше третьей.


def treug(n, m, k):
    sides = [n, m, k]
    sides.sort()
    return sides[0] + sides[1] > sides[2]

#   return max(n, m, k) < n + m + k - max(n, m, k)



for A in range(1, 300):
    flag = True
    for x in range(1, 300):
        f = not((treug(x, 11, 18) == (not (max(x, 5) > 68))) and treug(x, A, 5))
        if not f:
            flag = False

    if flag:
        print(A)