from ipaddress import ip_network

net = ip_network('0.0.0.0/255.255.255.128', 0)  # Айпи адрес дан не был
count = 0

# for i in net:
#     count += 1
#     print(net)
#
# print(count - 2)

print(net.num_addresses - 2)  # Считает кол-во айпи адрессов
