answers = []

for first_n in range(1, 200):
    n2_str = ''

    n = first_n
    # while n > 0:
    #     n2_str += str(n % 2)
    #     n //= 2
    # n2_str = n2_str[::-1]
    n2 = bin(n)[2:]

    if n2.count('1') % 2 == 0:
        n2 = '10' + n2[2:] + '0'
    else:
        n2 = '11' + n2[2:] + '1'

    r = int(n2, 2)

    if r >= 480:
        print(first_n, r)
        answers.append(r)

print(min(answers))

