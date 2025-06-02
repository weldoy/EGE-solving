with open('17_22468.txt') as file:
    numbers = [int(n) for n in file]
    av = sum(numbers) / len(numbers)
    arr = []
    for i in range(len(numbers) - 1):
        a, b = numbers[i], numbers[i+1]
        if abs(a + b) > av:
            arr.append(a + b)

print(len(arr), abs(min(arr)))
