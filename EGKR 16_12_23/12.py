def f(n: str):
    while ('11' in n) or ('444' in n) or ('8888' in n):
        if '11' in n:
            n = n.replace('11', '4', 1)
        elif '444' in n:
            n = n.replace('444', '88', 1)
        elif '8888' in n:
            n = n.replace('8888', '1', 1)
    return n

result = []
for x in range(4, 10001):
    n = '8' + '4' * x
    n = f(n)
    result.append(sum(int(i) for i in n))
    print(f'{n=} {x=}')

print(max(result))
