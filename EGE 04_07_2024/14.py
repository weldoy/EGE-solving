def to_six(n):
    string = ''
    while n > 0:
        string += str(n % 6)
        n //= 6
    return string


for x in range(1, 2031):
    a = 6**260 + 6**160 + 6**60 - x
    a = to_six(a)
    if a.count('0') == 202:
        print(x)
