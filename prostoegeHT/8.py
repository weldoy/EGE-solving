a = 'АЛПЦЯ'
lst = []
allw = []

count = 0
for x1 in a:
    for x2 in a:
        for x3 in a:
            for x4 in a:
                for x5 in a:
                    word = x1+x2+x3+x4+x5
                    if word.count('А') <= 1 and word.count('Ц') == 2 and word.count('Л') == 0:
                        lst.append(word)
                    count += 1
                    allw.append(word)
                    print(word, count)

print(allw.index('АППЦЦ') + 1)

