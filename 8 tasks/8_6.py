alphabet = '0123456789ABCDE'
count = 0
for q in '123456789ABCDE':
    for w in alphabet:
        for e in alphabet:
            for r in alphabet:
                for t in alphabet:
                    word = q+w+e+r+t
                    if (word.count('8') == 1 and
                            (word.count('A') + word.count('B') + word.count('C') +
                             word.count('D') + word.count('E')) >= 2):
                        count += 1
print(count)
