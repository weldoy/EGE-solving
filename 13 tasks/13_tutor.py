from ipaddress import *

net = ip_network('227.116.246.2/23', 0)  # Создание своего адреса сети
addr = ip_address('227.116.246.2')
iface = ip_interface('227.116.246.2/23')
print(net, addr, iface.network)  # iface.netword выдаст адрес сети, в которой сидит интерфейс
