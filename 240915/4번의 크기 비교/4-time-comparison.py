a = int(input())

arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] < a:
        print("1")
    else:
        print("0")