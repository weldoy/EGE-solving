from ipaddress import *

net = ip_network('227.116.246.2/255.255.224.0', 0)  # Создание своего адреса сети
print(net)
