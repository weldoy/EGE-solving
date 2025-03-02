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

# 2**15 комбинаций       10000000.00000000
# net  01110000.11010000.00000000.00000000
# mask 11111111.11111111.10000000.00000000

# count = 0
# for i in range(2**15):
#     if (6 + bin(i)[2:].count('1')) % 11 == 0:
#         count += 1
#
# print(f'{count}')
