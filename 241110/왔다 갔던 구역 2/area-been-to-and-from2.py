n = int(input())

arr = [0] * 200
now = 100

for i in range(n):
    x, W = tuple(map(str, input().split()))
    arr[now] += 1
    if W == "R":
        for j in range(int(x)):
            now += 1
            arr[now] += 1 
            #print(arr)
    else: 
        # 왼쪽으로 7
        for k in range(int(x)):
            now -= 1
            arr[now] += 1
            #print(arr)

result = 0
for i in range(len(arr)):
    if arr[i] >= 2:
        result += 1

print(result-1)