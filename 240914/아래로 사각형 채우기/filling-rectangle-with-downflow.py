n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        arr[j][i] = j * n + i + 1
        print(j * n + i + 1, end=" ")
    print()