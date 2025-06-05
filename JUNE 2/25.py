from fnmatch import fnmatch

count = 0
for i in range(84318, 10**12, 84318):
    if fnmatch(str(i), '5*7?'):
        if len(str(i)) == len(set(str(i))):
            print(i, i // 84318)
