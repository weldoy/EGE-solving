from ipaddress import ip_network

count = 0
net = ip_network("115.192.0.0/255.192.0.0")
for ip in net:
    binip = f'{int(ip):032b}'
    if binip.count('1') % 3 != 0:
        count += 1

print(count)