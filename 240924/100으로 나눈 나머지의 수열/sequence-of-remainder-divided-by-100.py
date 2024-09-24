# 2, 4, 2*4%100 ...

def get_num(n):
    if n == 1:
        return 2
    if n == 2:
        return 4
    return get_num(n-1) * get_num(n-2) % 100


n = int(input())
print(get_num(n))