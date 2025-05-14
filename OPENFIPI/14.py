for x in range(1, 2301):
    n = 7**350 + 7**150 - x
    ans = ''
    while n > 0:
        ans += str(n % 7)
        n //= 7
    ans = ans[::-1]
    if ans.count('0') == 200:
        print(x, ans)
