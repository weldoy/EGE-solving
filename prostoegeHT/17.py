with open('17_53I3OqE.txt') as f:
    numbers = [int(n) for n in f]

minelem = min(n for n in numbers)
ans = []

for i in range(len(numbers) - 1):
    a, b = numbers[i], numbers[i+1]
    if (a % 77) * (b % 77) == minelem**2:
        ans.append(a*b)

print(len(ans), min(ans))
