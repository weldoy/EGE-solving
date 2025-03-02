alphabet = 'INSP'
count = 0
for x1 in alphabet:
    for x2 in alphabet:
        for x3 in alphabet:
            for x4 in alphabet:
                for x5 in alphabet:
                    for x6 in alphabet:
                        for x7 in alphabet:
                            word = x1+x2+x3+x4+x5+x6+x7
                            if word.count('S') == 2 and word.count('IP') == 0:
                                count += 1

print(count)
