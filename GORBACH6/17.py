with open('17.txt') as f:
    arr = []
    numbers = [int(n) for n in f]
    div7 = min(int(i) for i in numbers if (abs(i) % 10 == 7 and abs(i) % 7 == 0))

    for i in range(len(numbers) - 1):
        a, b = numbers[i], numbers[i + 1]
        _a, _b = abs(numbers[i]), abs(numbers[i+1])

        if ((100 <= _a <= 999) or (100 <= _b <= 999)) and (a + b > div7):
            arr.append((a**2 + b**2))

    print(len(arr), max(arr))