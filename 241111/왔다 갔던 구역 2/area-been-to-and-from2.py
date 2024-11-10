n = int(input())

arr = [0] * 20
now = 10

for i in range(n):
    x, W = tuple(map(str, input().split()))
    #arr[now] += 1
    if W == "R":
        for j in range(1, int(x)):
            now += 1
            arr[now] += 1 
            #print(arr)
    else: 
        # 왼쪽으로 7
        for k in range(1, int(x)):
            now -= 1
            arr[now] += 1
            #print(arr)

result = 0
for i in range(len(arr)):
    if arr[i] >= 2:
        result += 1

print(result-1)