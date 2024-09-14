nm = list(map(int, input().split()))
#nm[0] 행열

arr = [[0 for _ in range(nm[0])] for _ in range(nm[0])]

for i in range(nm[1]):
    rc = tuple(map(int, input().split()))
    arr[rc[0]-1][rc[1]-1] = 1

for i in range(nm[0]):
    for j in range(nm[0]):
        print(arr[i][j], end=" ")
    print()