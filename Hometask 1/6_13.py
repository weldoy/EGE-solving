from ipaddress import ip_network

for A in range(16, 33):
    net = ip_network(f'252.63.194.3/{A}', 0)
    flag = True
    for ip in net:
        if not(f'{ip:b}'[:16].count('1') >= f'{ip:b}'[16:].count('1')):
            flag = False
    if flag:
        print(A)
