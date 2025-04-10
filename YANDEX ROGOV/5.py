n = 3
n3 = n
n3s = ''

while n3 > 0:
    n3s += str(n3 % 3)
    n3 //= 3
    reversed(n3s)

# if int(n3s) % 3 == 0:
n3s = n3s[0] + n3s[0] + n3s[1] + n3s[1] + n3s[2] + n3s[2] + n3s[3] + n3s[3] + n3s[4] + n3s[4] + n3s[5] + n3s[5] + n3s[6] + n3s[6]
print(n3s)