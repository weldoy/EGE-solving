with open('17.txt') as f:
    numbers = [int(n) for n in f]

max5 = max(i for i in numbers if abs(i) % 100 == 25)
maxs = 0
count = 0

for i in range(len(numbers) - 2):
    a, b, c = numbers[i], numbers[i+1], numbers[i+2]
    _a, _b, _c = abs(numbers[i]), abs(numbers[i + 1]), abs(numbers[i + 2])
    if ((1000<= _a <= 9999) + (1000<= _b <= 9999) + (1000<= _c <= 9999)) <= 2:
        if a+b+c <= max5:
            maxs = max(maxs, a+b+c)
            count += 1

print(count, maxs)
