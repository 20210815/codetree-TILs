n, m = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

def change(arr):
    sum = 0
    global m
    while m >= 1:
        sum += arr[m-1]
        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
    return sum


print(change(arr))