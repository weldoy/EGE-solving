with open('9') as f:
    numbers = []
    for n in f:
        n = n.split()
        numbers.append(n)
    # numbers = [int(line).split('\t') for line in f]
    print(numbers)
