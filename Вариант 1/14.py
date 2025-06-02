n = 3*17**777 + 15*17**250 - 6*17**100 + 2

s = ''
while n > 0:
    s += str(n % 17) + '.'
    n = n // 17

print(s.split('.'))
arr = set()
for i in s.split('.')[:-1]:
    if int(i) % 2 == 0:
        arr.add(int(i))

print(arr)
