import array

with open('17.txt') as file:
    numbers = [int(n) for n in file]

maxd = 0
for i in numbers:
    if len(str(i)) == 4:
        maxd = max(maxd, i)

arr = []

for i in range(len(numbers) - 1):
    a, b = numbers[i], numbers[i + 1]
    if abs(a - b) >= maxd:
        arr.append(a + b)

print(len(arr), max(arr))
