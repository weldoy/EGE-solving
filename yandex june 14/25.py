import fnmatch

# for i in range(1, 10**10):
#     if fnmatch.fnmatch(str(i), '10*2426?'):
#         if (i % 8465 == 0) or (i % 9799 == 0):
#             if i % (8465 * 9799):
#                 print(i, i // (8465 * 9799))
#             elif i % 8465 == 0:
#                 print(i, i // 8465)
#             elif i % 9799 == 0:
#                 print(i, i // 9799)


for i in range(0, 10**10, 8465):
    if fnmatch.fnmatch(str(i), '10*2426?'):
        print(i, i // 8465)


# for i in range(0, 10**10, 9799*8465):
#     if fnmatch.fnmatch(str(i), '10*2426?'):
#         print(i, i // 9799*8465)

