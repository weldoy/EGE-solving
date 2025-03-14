with open('17_8.txt') as f:
    numbers = [int(i) for i in f]
    arr = []
    for i in range(len(numbers) - 1):
        a, b = numbers[i], numbers[i+1]
        if a % 16 == min(numbers) or b % 16 == min(numbers):
            arr.append(a+b)
    print(len(arr), max(arr))
