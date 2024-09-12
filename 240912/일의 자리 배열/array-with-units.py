arr = list(map(int, input().split()))

for i in range(2, 10):
    sum = arr[i-2] + arr[i-1]
    if sum >= 10:
        result = sum % 10
        arr.append(result)
    else:
        arr.append(sum)

for i in range(10):
    print(arr[i], end=" ")