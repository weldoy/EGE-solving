# TUWXYZ МАКСИМАЛЬНОЕ ЗНАЧЕНИЕ

f = open(...).readline()

w = f.split('нужный символ')
cnt = 0
for i in range(len(f) - 'кол-во встречающихся раз + 1'):
    a = 'нужный символ'.join(w[i:i + 'кол-во встречающихся раз + 1'])
    m = max(len(a), m)

print(m)
