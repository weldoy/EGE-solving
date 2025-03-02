from ipaddress import *

cnt = 0
net = ip_network('192.168.32.48/255.255.255.240', False)

for ip in net:
    if f'{int(ip):032b}'.count('1') % 2 == 1:
        cnt += 1

print(f'Кол-во ip адрессов кратных двум = {cnt}')
