n = 9 * 57**2024 + 14 * 13**3059 - 87 * 67**1111 + 2027
s = ''
count = 0

while n > 0:
    s += f'{n % 36} '
    n //= 36

s = s.split()
print(s)

for i in s:
    if int(i) > 20:
        count += 1

print(count)
