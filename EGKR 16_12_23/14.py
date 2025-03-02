r = 4 * 3125**2019 + 3 * 625**2020 - 2 * 125**2021 + 25**2022 - 4 * 5**2023 - 2024

def to_base(n, base):
    result = []
    while n > 0:
        result.append(n % base)
        n //= base
    return result[::-1]

print(len([i for i in to_base(r, 25) if i > 10]))
