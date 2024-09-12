n = int(input())

arr = []
for i in range(1, 21):
    arr.append(n*i)

cnt = 0
for i in range(len(arr)):
    if cnt == 2:
        break
    if arr[i] % 5 == 0:
        cnt += 1
    print(arr[i], end=" ")