from ipaddress import ip_network

net = ip_network('116.29.170.89/255.255.255.224', False)

count = 0

for ip in net:
    ip2 = bin(int(ip))[2:]
    print(ip2[:16], ip2[16:], len(ip2))
    if ip2[:16].count('1') >= ip2[15:].count('1'):
        count += 1

print(count)
