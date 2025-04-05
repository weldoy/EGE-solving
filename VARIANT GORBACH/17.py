with open('17.txt') as f:
    numbers = [int(x) for x in f]
    # arr = [q for q in numbers if (q % 10 == 7 and q / 7 == 0)]
    answer = []
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            a, b = abs(numbers[i]), abs(numbers[j])
            if ((100 <= a <= 999) or (100 <= b <= 999)) and ((a+b) > 7):
                answer.append(a**2 + b**2)

print(len(answer), max(answer))
