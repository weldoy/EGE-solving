with open('17_17558.txt') as f:
    numbers = [int(line) for line in f]
    d_32 = [abs(num) for num in numbers if (abs(num) % 32 == 0)]
    answers = []
    for i in range(len(numbers) - 1):
        a, b = numbers[i], numbers[i+1]
        _a, _b = abs(numbers[i]), abs(numbers[i + 1])
        if (a < 0 or b < 0) and ((a + b) < len(d_32)):
            answers.append(a+b)

print(len(d_32))
print(len(answers), max(answers))
