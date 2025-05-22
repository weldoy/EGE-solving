with open('17_21903.txt') as f:
    numbers = [int(n) for n in f]

minsquare15 = min(n for n in numbers if ((abs(n) % 100 == 15) and (100 <= abs(n) <= 999))) ** 2

arr = []
for i in range(len(numbers) - 2):
    a, b, c = numbers[i], numbers[i+1], numbers[i+2]
    lst = sorted([a, b, c])
    if (((a >= 0) and (b >= 0) and (c >= 0)) or ((a <= 0) and (b <= 0) and (c <= 0))) and \
            ((lst[0] * lst[2]) > minsquare15):
        arr.append(lst[0] * lst[2])

print(len(arr), min(arr))
