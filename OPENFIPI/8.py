alphabet = '0123456789'
count = 0


def f(x: str):
    evens = '02468'
    odds = '13579'
    for i in range(len(x) - 1):
        if x[i] in evens and x[i+1] in evens:
            return False
        if x[i] in odds and x[i+1] in odds:
            return False
    return True


for x1 in alphabet:
    for x2 in alphabet:
        for x3 in alphabet:
            for x4 in alphabet:
                word = x1+x2+x3+x4
                if f(word):
                    count += 1

print(count)
