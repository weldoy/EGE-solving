alphabet = 'АЙЛМ'
count = 0

for x1 in alphabet:
    for x2 in alphabet:
        for x3 in alphabet:
            for x4 in alphabet:
                for x5 in alphabet:
                    word = x1+x2+x3+x4+x5
                    count += 1
                    if word.count('М') == 0 and word.count('Л') == 0 and word.count('ЙЙ') == 0:
                        print(word, count)
