with open('24_3.txt') as f:
    line = f.readline().strip()

alphabet = '0123456789AB'
max_line = 0

for i in range(len(line)):
    if line[i] in alphabet[1:]:
        counter = 0
        j = i
        try:
            while line[j+1] in alphabet:
                j += 1
                counter += 1
                # print(f'{line[j]=} {counter=}')
            if counter > max_line:
                max_line = max(counter, max_line)
                # print(f'{max_line=} {line[i:j]}')
        except IndexError:
            print('index out of range')
print(max_line)

