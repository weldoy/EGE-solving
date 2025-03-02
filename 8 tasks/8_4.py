alphabet = 'ТРОЙКА'
count = 0

for x1 in alphabet:
    for x2 in alphabet:
        for x3 in alphabet:
            for x4 in alphabet:
                for x5 in 'ТРОЙА':
                    word = x1+x2+x3+x4+x5
                    if word.count('О') + word.count('А') >= 2:
                        count += 1
                        print(word, count)