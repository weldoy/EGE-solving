b = range(14, 21)
c = range(15, 28)

answers = set()
for left_a in range(1, 100):
    for right_a in range(left_a + 1, 101):
        a = range(left_a, right_a + 1)
        flag = True
        for x in range(1, 1000):
            if not(not(x in a) <= ((x in b) == (x in c))):
                flag = False
        if flag:
            answers.add(len(a) - 1)
print(sorted(answers))
