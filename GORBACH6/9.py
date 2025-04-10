with open('9') as f:
    count = 0
    # numbers = [int(s) for s in f]
    # for i in range(len(numbers) - 6):
    #     x1, x2, x3, x4, x5, x6 = numbers[i], numbers[i+1], numbers[i+2], numbers[i+3], numbers[i+4], numbers[i+5]
    numbers = [line for line in f]
    for line in numbers:
        line = line.split()
        if (line.count(line[0]) == 3 or line.count(line[1]) == 3 or
                line.count(line[2]) == 3 or line.count(line[3]) == 3 or
                line.count(line[4]) == 3 or line.count(line[5]) == 3) and (line.count(min(line)) > 1):
            count += 1
            print(line)

print(count - 2)
