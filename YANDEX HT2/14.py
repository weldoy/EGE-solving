n = 7 * 512**120 - 6 * 64**100 + 8**210 - 255


def f(x, y):
    result = ''
    while x > 0:
        result += str(x % y)
        x //= y
    return result[::-1]


for i in range(1000000000, 10000000000):
    if f(n, i)[-3:] == '001':
        print(i)
