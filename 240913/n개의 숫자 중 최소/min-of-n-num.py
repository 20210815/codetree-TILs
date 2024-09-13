n = int(input())

arr = list(map(int, input().split()))

min_val = arr[0]
for i in range(1, n):
    if min_val > arr[i]:
        min_val = arr[i]

print(min_val, arr.count(min_val))