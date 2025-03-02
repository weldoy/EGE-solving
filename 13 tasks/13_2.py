from ipaddress import *

for i in range(0, 32 + 1):  # Маска может быть максимум 32 единички
    try:
        net = ip_network('111.81.192.0/' + str(i))  # Адрес сети
        if ip_address('111.81.208.27') in net:
            print(f'net = {net.netmask} / {i=}')
    except:
        pass

# Найти наименьший 3 слева байт в маске
# Ответ (net = 255.255.192.0 / i=18) - ! 192 !
