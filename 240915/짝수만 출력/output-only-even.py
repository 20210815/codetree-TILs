arr = list(map(int, input().split()))


while arr[1] >= arr[0]:
    print(arr[0], end=" ")
    arr[0] += 2