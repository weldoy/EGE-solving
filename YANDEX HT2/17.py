def func(x, y, z):
    if (x > 0) and (y < 0) and (z < 0):
        return True
    if (x < 0) and (y > 0) and (z < 0):
        return True
    if (x < 0) and (y < 0) and (z > 0):
        return True
    return False


with open('17.txt') as f:
    numbers = [int(n) for n in f]
    sortednumbers = sorted(numbers)

arr = []
for i in range(len(numbers) - 2):
    a, b, c = numbers[i], numbers[i+1], numbers[i+2]
    # _a, _b, _c = abs(numbers[i]), abs(numbers[i+1]), abs(numbers[i+2])
    lst = sorted([a, b, c])
    if (func(a, b, c)) and ((a * b * c) <= (sortednumbers[-2] * sortednumbers[-1])):
        arr.append(a+b+c)

print(len(arr), max(arr))

