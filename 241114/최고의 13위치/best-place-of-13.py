N = int(input())

arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

max_cnt = 0
for i in range(N):
    for j in range(N-2):
        # 동전 담기
        # 1, 3 arr[i][j] + arr[i][j+1] + arr[i][j+2]
        max_cnt = max(max_cnt, arr[i][j] + arr[i][j+1] + arr[i][j+2])

print(max_cnt)