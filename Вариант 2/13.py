def mask(n):
    return ((2**32-1) << n) & (2**32 - 1)


ip = (192 << 24) + (214 << 16) + (116 << 8) + 184
q = 0

for n in range(33):
    net = ip & mask(n)
    q += f'{net : b}'.count('1') % 5 == 0 and (ip & (2**n - 1)) != (2**n - 1) and ip != net

print(q)
