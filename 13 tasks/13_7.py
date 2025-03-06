from ipaddress import *

net = ip_network('211.46.0.0/255.255.128.0', 0)
count = 0
for ip in net:
    ip1 = str(bin(int(ip))[2:])
    if ip1.count('1') % 4 == 0 and ip1[-2:] == '11':
        count += 1

print(count)
