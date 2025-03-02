answer = []

with open('somefile.txt') as file:
    numbers = [int(line) for line in file]

for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        a, b = numbers[i], numbers[j]
        if abs(a + b) % 10 == 0:
            answer.append(a + b)

print(f'{len(numbers)=}, {max(answer)=}')
