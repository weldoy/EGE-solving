from ipaddress import *

net = ip_network('10.18.134.220/255.255.255.192', 0)
k = -1  # Чтобы не считать нули

for ad in net:
    k += 1
    if ad == ip_address('10.18.134.220'):
        print(k)
        break
