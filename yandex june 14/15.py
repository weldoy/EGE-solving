b = range(1, 10000)
c = range(3648, 6288)

answer = []

for left_A in range(1, 100):
    for right_A in range(left_A + 1, 101):
        A = range(left_A, right_A + 1)
        flag = True
        for x in range(4201, 10000):
            if not (((x in b) == (x in c)) or (x in A) or (x > 4200)):
                flag = False
        if flag:
            answer.append(len(A) - 1)

print(sorted(answer))
