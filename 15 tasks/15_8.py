def f(x):
    return (x in Q) <= ((x in P) <= (x in Q) and A)


Q = [q for q in range(1, 10000) if q % 3 == 0]
P = [p for p in range(1, 10000) if p % 5 == 0]

answer = []

for A in range(1, 1000):
    if all(f(x) for x in range(1, 100)):
        answer.append(A)

divisors = set()
count = 0
for i in range(2, int(len(answer)**0.5)):
    if answer[count] % i == 0:
        divisors.add(i)
    if (answer[count] // i) % i == 0:
        divisors.add(i)
    count += 1

print(max(divisors))
