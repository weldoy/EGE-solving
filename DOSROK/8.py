alphabet = 'ДГИАШЭ'
counter = 0

for x1 in 'ДГШ':
    for x2 in alphabet:
        for x3 in alphabet:
            for x4 in alphabet:
                for x5 in 'ИАЭ':
                    counter += 1
print(counter)
