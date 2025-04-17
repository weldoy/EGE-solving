with open('24_4.txt') as f:
    line = f.readline().strip()

digits = '06789'
max_line = 0
try:
    for i in range(len(line) + 1):
        if line[i] in digits:
            counter = 0
            j = i
            try:
                while line[j+1] in digits:
                    j += 1
                    counter += 1
                # max_line = max(max_line, counter)
                if counter > max_line:
                    max_line = max(counter, max_line)
                    print(f'{max_line=} {line[i:j+1]}')

            except IndexError:
                print('Index [j] out of range')
except IndexError:
    print('Index [i] out of range')
