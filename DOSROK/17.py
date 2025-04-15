with open('17.txt') as f:
    answer = []
    numbers = [int(n) for n in f]
    sum_negative = sum(int(i) for i in numbers if int(i) < 0)
    for i in range(len(numbers) - 2):
        a, b, c = numbers[i], numbers[i+1], numbers[i+2]
        # _a, _b, _c = abs(numbers[i]), abs(numbers[i+1]), abs(numbers[i+2])
        lst = [a, b, c]

        if (max(lst) * min(lst)) > sum_negative:
            answer.append(a+b+c)

    print(len(answer), abs(max(answer)))
