from ipaddress import ip_network, ip_address

for mask in range(0, 33):
    net = ip_network('98.162.71.94/' + str(mask), 0)
    if net.network_address == ip_address('98.162.71.64'):
        print(mask, net.num_addresses)
