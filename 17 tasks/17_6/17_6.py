with open('17_6.txt') as f:
    numbers = [int(i) for i in f]
    arr = []
    count = 0
    for i in numbers:
        if str(i)[-1] == '7':
            count += 1
    for i in range(len(numbers) - 1):
        a, b = numbers[i], numbers[i+1]
        if ((a > 0 > b) or (a < 0 < b)) and (a + b) < count:
            arr.append(a+b)

    print(len(arr), max(arr))
