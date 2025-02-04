from ipaddress import ip_network

net = ip_network('112.208.0.0/255.255.128.0')
ip_count = 0
for ip in net:
    count = 0
    for i in f'{int(ip):032b}':
        count += int(i)
    if count % 11 == 0:
        ip_count += 1

print(ip_count)