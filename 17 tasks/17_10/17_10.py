with open('17_9786.txt') as f:
    numbers = [int(n) for n in f]

answer = []

max25 = -10**10
for i in numbers:
    if abs(i) % 100 == 25:
        max25 = max(max25, i)

for i in range(len(numbers) - 2):
    a, b, c = numbers[i], numbers[i+1], numbers[i+2]
    if ((1000 <= abs(a) <= 9999) + (1000 <= abs(b) <= 9999) + (1000 <= abs(c) <= 9999)) <= 2:
        if a+b+c <= max25:
            answer.append(a+b+c)

print(len(answer), max(answer))
