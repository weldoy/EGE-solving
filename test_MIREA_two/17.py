with open('17var15.txt') as f:
    answers = []
    numbers = [int(num) for num in f]
    for i in range(len(numbers) - 1):
        a, b = numbers[i], numbers[i+1]
        _a, _b = abs(numbers[i]), abs(numbers[i + 1])
        if 100 <= (_a + _b) <= 700:
            answers.append(_a + _b)

    print(len(answers), max(answers))
