arr = list(map(int, input().split()))

for i in range(10):
    if arr[i] == 0:
        arr = arr[:i]
        break

print("%d %.1f" %(sum(arr), sum(arr)/len(arr)))