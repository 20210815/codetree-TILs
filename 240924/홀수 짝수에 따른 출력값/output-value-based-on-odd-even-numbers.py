def get_num(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return n + get_num(n-2)




n = int(input())
print(get_num(n))