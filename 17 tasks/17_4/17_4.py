with open('17_4.txt') as f:
    numbers = [int(i) for i in f]
    arr = 0
    abb = []
    for a in range(len(numbers)):
        if numbers[a] % 32 == 0:
            arr += 1
    for i in range(len(numbers) - 1):
        a, b = numbers[i], numbers[i+1]
        if (a < 0 or b < 0) and (a + b) < arr:
            abb.append(a+b)
    print(len(abb), max(abb))
