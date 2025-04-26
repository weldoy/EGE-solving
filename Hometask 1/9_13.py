from ipaddress import ip_network

for A in range(0, 256):
    net = ip_network(f'32.0.{A}.5/255.255.240.0', 0)
    flag = True
    for ip in net:
        if (f'{int(ip):b}'[:16].count('1')) < (f'{int(ip):b}'[16:].count('1')):
            flag = False
    if flag:
        print(A)
