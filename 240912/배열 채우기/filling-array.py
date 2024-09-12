arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        arr = arr[:i]
        break

for j in range(len(arr), 0, -1):
    print(arr[j-1], end=" ")