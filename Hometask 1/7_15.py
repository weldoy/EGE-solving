b = range(10, 16)
c = range(20, 28)

answers = set()
for left_a in range(1, 100):
    for right_a in range(left_a + 1, 101):
        a = range(left_a, right_a + 1)
        flag = True
        for x in range(1, 1000):
            if not(((x in b) or (x in c)) <= (x in a)):
                flag = False
        if flag:
            answers.add(len(a) - 1)
print(sorted(answers))
