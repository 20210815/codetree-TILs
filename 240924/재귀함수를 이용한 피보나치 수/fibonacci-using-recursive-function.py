def get_phi(n):
    if n == 1:
        return 1
    elif n < 1:
        return 0
    return get_phi(n-1) + get_phi(n-2)

n = int(input())
print(get_phi(n))