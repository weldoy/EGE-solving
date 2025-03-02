from itertools import *

count = 0
for i in product('ABCDE', repeat=4):
    if (str(i[0]) != 'A' or str(i[0]) != 'E') and ('BE' not in ''.join(i) and 'EB' not in ''.join(i)):
        if 'D' in ''.join(i):
            if 'DB' in ''.join(i) or 'BD' in ''.join(i):
                count += 1
            else:
                count = count
        else:
            count += 1
print(count)
