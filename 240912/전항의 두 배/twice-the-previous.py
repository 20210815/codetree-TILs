arr = list(map(int, input().split()))

for i in range(0,8):
    sum = 2*arr[i] + arr[i+1]
    arr.append(sum)

for i in range(len(arr)):
    print(arr[i], end=" ")