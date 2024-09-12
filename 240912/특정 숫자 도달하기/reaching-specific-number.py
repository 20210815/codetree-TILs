arr = list(map(int, input().split()))

sum = 0
for i in range(len(arr)+1):
    if arr[i] < 250:
        sum += arr[i]
    else:
        break

print("%d %.1f" %(sum, sum/(i)))