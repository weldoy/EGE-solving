for n in range(1, 10000):
    string = ''

    while n > 0:
        string += str(n % 5)
        n //= 5

    string = string[::-1]

    if int(string) % 25 == 0:
        string += string[-3::]
    else:
        m_str = ''
        m = int(string) % 25
        while m > 0:
            m_str += str(m % 5)
            m //= 5
        string += m_str[::-1]

        if int(string, 5) > 10000:
            print(n)
