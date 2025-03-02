n = '7' * 85 + '5'

while '775' in n or '575' in n or '57' in n:
    if '775' in n:
        n = n.replace('775', '57', 1)
    if '575' in n:
        n = n.replace('575', '7', 1)
    if '77' in n:
        n = n.replace('77', '5', 1)
    if '55' in n:
        n = n.replace('55', '7', 1)

print(n)
