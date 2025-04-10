from functools import lru_cache


@lru_cache()
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return n * (n - 1) + f(n - 1) - f(n - 2)


for n in range(1, 2025):
    f(n)


print(f(2024) + f(2020) - f(2019))
