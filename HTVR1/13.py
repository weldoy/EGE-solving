from ipaddress import ip_network

net = ip_network('172.16.192.0/255.255.192.0', 0)
count = 0

for ip in net:
    ipb = bin(int(ip))[2:]
    if ipb.count('1') % 5 != 0:
        count += 1

print(count)
