with open('24_2.txt') as f:
    line = f.readline().strip()
    positions = []
    template = 'FSRQ'
    for i in range(len(line) - 3):
        if line[i:i+4] == template:
            positions.append(i)

    max_len = 0
    for i in range(len(positions) - 80):
        length = positions[i + 79] - positions[i] + 3
        if i > 0:
            length += positions[i] - positions[i-1] - 1
        elif (i + 80) == len(positions):
            length += positions[i+80] - positions[i+79] + 2
        max_len = max(max_len, length)

print(max_len)
