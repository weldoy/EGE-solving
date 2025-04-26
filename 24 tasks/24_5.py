with open('24_5.txt') as f:
    line = f.readline().strip()

# positions = []
# alphabet = '0789'
# for pos in range(len(line)):
#     if line[pos] not in alphabet:
#         positions.append(pos)
# positions.sort()

left = 0
right = left + 1
maxline = 0
while right < len(line):
    count = 0
    if line[right] in ('0789', '*-'):
        if line[right+1] in '*-':
            cut = line[left:right]
            maxline = max(maxline, len(cut))
            
