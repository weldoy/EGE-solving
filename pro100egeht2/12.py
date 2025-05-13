n = '>' + (10*'1') + (20*'2') + (30*'3')

while ('>1' in n) or ('>2' in n) or ('>3' in n):
    if '>1' in n:
        n = n.replace('>1', '22>', 1)
    if '>2' in n:
        n = n.replace('>2', '2>', 1)
    if '>3' in n:
        n = n.replace('>3', '1>', 1)

summ = 0
for i in n[:-1]:
    summ += int(i)

print(summ)
