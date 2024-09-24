def get_fac(n):
    if n == 1:
        return 1
    return n * get_fac(n-1)

n = int(input())

print(get_fac(n))