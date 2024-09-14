n = int(input())

arr = [[1 for j in range(i+1)] for i in range(n)]

#print(arr)
for i in range(1, n):
    for j in range(1, i):
        arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

for i in range(n):
    for j in range(i+1):
        print(arr[i][j], end=" ")
    print()