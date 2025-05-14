def f(x: str):
    evens = '02468'
    odds = '13579'
    for i in range(len(x) - 1):
        if (x[i] in evens) and (x[i+1] in evens):
            return False
        if (x[i] in odds) and (x[i+1] in odds):
            return False
    return True


count = 0

for x1 in '0123456789':
    for x2 in '0123456789':
        for x3 in '0123456789':
            for x4 in '0123456789':
                word = x1+x2+x3+x4
                lst = []
                for i in word:
                    lst.append(int(i))
                if all([f(word), len(set(lst)) == 4]):
                    count += 1
                    print(word, count, f(word), len(set(lst)))

print(count)
