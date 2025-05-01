p = range(117, 159)
q = range(129, 181)


def f(x):
    return (x in p) <= (((x in q) and (x not in a)) <= (x not in p))


answer = []
for a_left in range(1, 100):
    for a_right in range(a_left + 1, 101):
        a = range(a_left, a_right + 1)
        flag = True
        for x in range(1, 1000):
            if not f(x):
                flag = False
        if flag:
            answer.append(len(a) - 1)
print(sorted(answer))
