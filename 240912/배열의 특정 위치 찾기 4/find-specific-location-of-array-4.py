arr = list(map(int, input().split()))

new_arr = []
for i in range(10):
    if arr[i] == 0:
        break
    elif arr[i] % 2 == 0:
        new_arr.append(arr[i])

print("%d %d" %(len(new_arr), sum(new_arr)))