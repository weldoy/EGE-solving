with open('17_lUDh3Lh.txt') as f:
    numbers = [int(n) for n in f]

average = sum(i for i in numbers) / len(numbers)
answer = []

for i in range(len(numbers) - 1):
    a, b = numbers[i], numbers[i + 1]
    if (a > average) or (b > average):
        answer.append(a+b)

print(len(answer), max(answer))
