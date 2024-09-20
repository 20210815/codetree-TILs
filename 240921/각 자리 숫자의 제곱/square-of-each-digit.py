n = int(input())

def mul(n):
    if n < 10:
        return n ** 2
    return mul(n // 10) + ((n % 10)**2)

print(mul(n))