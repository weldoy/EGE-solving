f = open('9_8pry8SC.csv')

count = 0

for i in f:
    x = sorted(list(map(int, i.split(','))))
    prog = x[3] - x[2]
    if (x[3]**2 > (x[0] * x[1] * x[2])) or ((x[0] + prog == x[1]) and (x[1] + prog == x[2]) and (x[2] + prog == x[3])):
        count += 1

print(count)
