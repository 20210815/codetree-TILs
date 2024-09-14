nm = list(map(int, input().split()))

arr = [[0 for _ in range(nm[0])] for _ in range(nm[0])]

for i in range(nm[1]):
    rc = tuple(map(int, input().split()))
    arr[rc[0]-1][rc[1]-1] = i + 1

for i in range(nm[0]):
    for j in range(nm[0]):
        print(arr[i][j], end=" ")
    print()