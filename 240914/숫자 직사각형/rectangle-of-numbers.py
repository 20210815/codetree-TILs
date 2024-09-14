a = list(map(int, input().split()))

arr = [[j * a[1] +1 + i for i in range(a[1])]
        for j in range(a[0])]

for i in range(a[0]):
    for j in range(a[1]):
        print(arr[i][j], end=" ")
    print()