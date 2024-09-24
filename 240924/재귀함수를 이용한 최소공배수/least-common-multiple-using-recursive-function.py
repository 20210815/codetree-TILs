n = int(input())
arr = list(map(int, input().split()))


# 1 2 3 4 5 6 7 8 9 10
#       2   3   4    5

def get_lmd(n):
    if n == 0:
        return arr[0]
    return arr[n] * get_lmd(n-1)