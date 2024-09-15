arr = list(map(str, input().split()))

sum = 0
for i in range(10):
    sum += len(arr[i])

print(sum)