n = int(input())

arr = [0] * 40
now = 20

for i in range(n):
    x, W = tuple(map(str, input().split()))
    if W == "R":
        for j in range(int(x)+1):
            now += 1
            arr[now] += 1 
    else:
        for k in range(int(x)+1):
            now -= 1
            arr[now] += 1

print(arr)

result = 0
for i in range(len(arr)):
    if arr[i] >= 2:
        result += 1

print(result)