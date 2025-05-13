alphabet = 'АЙЛМ'
count = 0
arr = []

for x1 in alphabet:
    for x2 in alphabet:
        for x3 in alphabet:
            for x4 in alphabet:
                for x5 in alphabet:
                    word = x1+x2+x3+x4+x5
                    count += 1
                    print(count, word)
                    if word.count('ЛЛ') == 0 and word.count('М') <= 1:
                        arr.append(count)
print(max(arr))
