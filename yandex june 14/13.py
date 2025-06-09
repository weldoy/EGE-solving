from ipaddress import ip_network

net = ip_network('192.168.0.0/255.255.192.0', False)
count = 0

for ip in net:
    if bin(int(ip))[2:].count('1') > bin(int(ip))[2:].count('0'):
        count += 1

print(count)
