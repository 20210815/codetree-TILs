# 1, 2, ..., arr[n//3] + arr[n-1]





def get_num(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return get_num(n//3) + get_num(n-1)


n = int(input())
print(get_num(n))