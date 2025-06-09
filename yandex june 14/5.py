arh = []

for first in range(1, 300):
    n = first
    result = ''
    while n > 0:
        result += str(n % 3)
        n //= 3
    sorted(result)
    r = 0
    while result[r] == '0':
        result = result[r + 1:] + '0'
    result = result + result[0]
    arh.append(int(result, 3))
    print(first, int(result, 3))

print(sorted(arh))
