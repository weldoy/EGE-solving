from ipaddress import *
arr = set()
for A in range(0, 256):
    net = ip_network(f'135.{A}.170.5/255.255.0.0', 0)
    for ip in net:
        ip_b = str(bin(int(ip))[2:])[:16]
        if ip_b.count('1') > 10:
            arr.add(A)

print(min(arr))
