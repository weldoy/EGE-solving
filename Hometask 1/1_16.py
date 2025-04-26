from functools import lru_cache


@lru_cache(None)
def f(x):
    if x == 1:
        return 1
    if x > 1:
        return x + f(x - 1)


for i in range(3000): f(i)

print(f(3000) - f(2000))
