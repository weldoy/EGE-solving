count = 0
alphabet = 'БЛОГЕР'

for x1 in alphabet:
    for x2 in alphabet:
        for x3 in alphabet:
            for x4 in alphabet:
                word = x1+x2+x3+x4
                if word.count('Г') == 1 and word.count('ОЕ') == 0 and word.count('ЕО') == 0 and word.count('ЕЕ') == 0 and word.count('ОО') == 0:
                    count += 1
                    print(count, word)
