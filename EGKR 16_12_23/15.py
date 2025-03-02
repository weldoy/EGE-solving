list_A = []

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not (x % A != 0 <= ((x % 28 == 0) <= (x % 9 != 0))):
            flag = False
    if flag:
        print(A)

# print(list_A)
