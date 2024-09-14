n = int(input())

arr = [0] * n

for i in range(n):
    arr[i] = list(map(int, input().split()))

sum = 0
for i in range(1, n-1):
    for j in range(1, n-1):
        if arr[i+1][j] + arr[i-1][j] + arr[i][j-1] + arr[i][j+1] >= 3:
            sum+=1


for i in range(1):
    for j in range(1, n-1):
        if arr[i+1][j] + arr[i][j+1] + arr[i][j-1] >= 3:
            sum +=1
        if arr[j+1][i] + arr[j][i+1] + arr[j-1][i] >= 3:
            sum += 1

for i in range(n-1, n):
    for j in range(1, n-1):
        if arr[i][j+1] + arr[i-1][j] + arr[i][j-1] >= 3:
            sum +=1
        if arr[j+1][i] + arr[j][i-1] + arr[j-1][i] >= 3:
            sum +=1

print(sum)



# (1,1) / (0,1) (2,1) / (1,0) (1,2)
# (0,0) / (-1,0)(1,0) / (0,-1)(0,1)