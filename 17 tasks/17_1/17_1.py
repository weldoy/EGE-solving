answer = []

with open('EGE/17 tasks/17_1/17_10719.txt') as f:
    numbers = [int(line) for line in f]

for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        a, b = numbers[i], numbers[j]
        if str(abs(a + b))[-1] == 3 and str(abs(a + b))[-2] == 1:
            answer.append(a + b)

print(f'{len(answer)=} {max(answer)}')
