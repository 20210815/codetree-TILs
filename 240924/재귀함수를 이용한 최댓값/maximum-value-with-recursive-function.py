def get_max(n):
    if n == 0:
        return arr[0]
    return max(arr[n], get_max(n-1))






n = int(input())
arr = list(map(int, input().split()))
print(get_max(n-1))