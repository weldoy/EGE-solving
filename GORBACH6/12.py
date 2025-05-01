for n in range(1, 100):
    for j in range(1, 100):
        for k in range(1, 100):

            nds = '7' * n + '8' * j + '9 tasks' * k
            nd = nds
            answer = 0

            while '78' in nd or '98' in nd or '999' in nd:
                if '78' in nd:
                    nd = nd.replace('78', '8', 1)
                if '798' in nd:
                    nd = nd.replace('798', '7', 1)
                if '999' in nd:
                    nd = nd.replace('999', '9 tasks', 1)
            for i in nd:
                answer += int(i)
            if answer == 801:
                print(n, len(nds), answer)
