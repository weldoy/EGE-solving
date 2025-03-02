n = 16**328 - 64**12 + 8**1021 - 2**349 + 29 * 2**34 - 7
string = ''

while n > 0:
    string += str(n % 4)
    n //= 4

print(string.count('3'))