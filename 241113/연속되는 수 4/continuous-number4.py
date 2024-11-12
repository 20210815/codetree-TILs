n = int(input())

arr = []
for test in range(n):
    arr.append(int(input()))

cnt = 0
max_cnt = 0
for i in range(1, n):
    if arr[i] > arr[i-1]:
        cnt += 1
    else:
        cnt = 1
    if cnt > max_cnt:
        max_cnt = cnt
        
print(max_cnt)