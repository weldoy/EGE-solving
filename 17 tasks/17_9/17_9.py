with open('17_9.txt') as f:
    numbers = [int(i) for i in f]

max43 = 0
count = 0
mins = 10**10

for i in numbers:
    if abs(i) % 100 == 43:
        if 10000 <= abs(i) <= 99999:
            max43 = max(max43, i)

for i in range(len(numbers) - 2):
    a, b, c = numbers[i], numbers[i+1], numbers[i+2]
    _a, _b, _c = abs(numbers[i]), abs(numbers[i+1]), abs(numbers[i+2])
    if ((10000 <= _a <= 99999 and _a % 100 == 43) + (10000 <= _b <= 99999 and _b % 100 == 43) +
        (10000 <= _c <= 99999 and _c % 100 == 43)) >= 1:
        if a**2 + b**2 + c**2 <= max43**2:
            count += 1
            mins = min(a**2 + b**2 + c**2, mins)

print(count, mins)