arr = list(map(int, input().split()))

if arr[0] <= 0:
    print("0")
else:
    for i in range(arr[1]):
        print(arr[0], end="")