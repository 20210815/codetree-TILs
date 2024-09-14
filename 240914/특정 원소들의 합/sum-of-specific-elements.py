arr = [0] * 4

for i in range(4):
    arr[i] = list(map(int, input().split()))

sum = 0
for i in range(4):
    for j in range(i+1):
        sum += arr[i][j]
print(sum)