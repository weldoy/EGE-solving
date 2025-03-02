string = '9' * 134

while '22222' in string or '9999' in string:
    print(string)
    if '22222' in string:
        string = string.replace('22222', '99', 1)
    elif '9999' in string:
        string = string.replace('9999', '2', 1)

print(string)
