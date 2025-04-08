n0 = 9*57**2024 + 14*13**3059 - 87*67**1111 + 2027

n = n0
s = []
while n > 0:
    s.append(int(n % 36))
    n //= 36

count = 0
for i in s:
    if i > 20:
        count += 1

print(count)

