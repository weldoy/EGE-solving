with open('24.txt') as f:
    line = f.readline().strip()

alphabet = '0123456789AB'
max_line = 0
try:
    for i in range(len(line) + 1):
        if line[i] in alphabet[1:]:
            j = i
            counter = 0
            while line[j+1] in alphabet:
                j += 1
                counter += 1

            if counter > max_line:
                max_line = max(max_line, counter)
                print(f'{max_line=} {line[i:j]=}')

except IndexError:
    print('Index out of range')

print(f'{max_line=}')
