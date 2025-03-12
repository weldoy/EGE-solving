with open('17_5.txt') as f:
    numbers = [int(i) for i in f]
    count_32 = 0
    arr = []
    for j in numbers:
        if j % 32 == 0:
            count_32 += 1
    for i in range(len(numbers) - 1):
        a, b = numbers[i], numbers[i+1]
        if (a < 0 or b < 0) and (a+b) < count_32:
            arr.append(a+b)
    print(len(arr), max(arr))
