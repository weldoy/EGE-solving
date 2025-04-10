count = 0
for x1 in 'XYZ':
    for x2 in 'XYZ':
        for x3 in 'XYZ':
            for x4 in 'XYZ':
                for x5 in 'XYZ':
                    word = x1+x2+x3+x4+x5
                    if word.count('X') == 2:
                        count += 1
                        print(count, word)
