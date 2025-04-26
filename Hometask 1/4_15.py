b = range(30, 42)
c = range(50, 57)

answer = set()
for a_left in range(1, 100):
    for a_right in range(a_left + 1, 101):
        a = range(a_left, a_right + 1)
        flag = True
        for x in range(1, 1000):
            f = not(((x in b) or (x in c)) <= (x in a))
            if f:
                flag = False
        if flag:
            answer.add(len(a) - 1)
print(sorted(answer))
