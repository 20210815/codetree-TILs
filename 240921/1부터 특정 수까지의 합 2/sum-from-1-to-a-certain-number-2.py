n = int(input())

def cal_sum(n):
    if n == 1:
        return 1
    return cal_sum(n-1) + n


print(cal_sum(n))