from ipaddress import *

net = ip_network('172.16.160.0/255.255.240.0', 0)
count = 0

for ip in net:
    ip2 = bin(int(ip))[2:]
    print(ip2)
    if ip2.count('1') % 4 != 0:
        count += 1

print(count - 2)
