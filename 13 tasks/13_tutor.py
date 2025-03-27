from ipaddress import *

net = ip_network('227.116.246.2/23', 0)  # Адрес узла
addr = ip_address('227.116.246.2')  # Адрес сети
iface = ip_interface('227.116.246.2/23')
print(net, addr, iface.network)  # iface.network выдаст адрес сети, в которой сидит интерфейс
print(net.network_address)  # Адрес сети выведет
print(net.num_addresses)  # Кол-во адресов
print(net.netmask)  # Маска сети
