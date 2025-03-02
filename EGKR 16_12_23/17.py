with open('17_16383.txt') as f:
    numbers = [int(line) for line in f]

for i in range(len(numbers) - 1):
    a, b = numbers[i], numbers[i + 1]
    if (a % 100 == 21) and (b % 100 != 21) or (b % 100 == 21) and (a % 100 != 21):
        pass

#     НЕ ЗАКОНЧЕНО

