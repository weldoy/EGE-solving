def f(n):
    return n if n >= 2025 else n + 3 + f(n+3)


print(f(2018) - f(2022))
