stp = 999

arr = list(map(int,input().split()))

min_val = arr[0]
max_val = arr[0]
for i in range(1, len(arr)):
    if arr[i] == stp or arr[i] == -stp:
        break
    if max_val < arr[i]:
        max_val = arr[i]
    if min_val > arr[i]:
        min_val = arr[i]
print(max_val, min_val)