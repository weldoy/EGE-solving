from ipaddress import ip_network

for A in range(16, 33):
    net = ip_network(f'191.239.130.3/{A}', 0)
    flag = True
    for ip in net:
        if not(f'{int(ip):b}'[:16].count('1') >= f'{int(ip):b}'[16:].count('1')):
            flag = False
    if flag:
        print(A)
