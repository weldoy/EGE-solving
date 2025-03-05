with open('17_3.txt') as f:
    numbers = [int(i)**2 for i in f]
    av_s = (sum(numbers) / len(numbers))**0.5
    arr = []
    for i in range(len(numbers) - 1):
        a, b = numbers[i]**0.5, numbers[i+1]**0.5
        if (a + b) >= av_s:
            arr.append(a+b)


print(len(arr), max(arr))
