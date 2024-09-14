c = list(map(int, input().split()))
# 행, 열

arr = [0] * c[0]
brr = [0] * c[0]
for i in range(c[0]):
    arr[i] = list(map(int,input().split()))

for i in range(c[0]):
    brr[i] = list(map(int,input().split()))


result = [[0 for _ in range(c[1])] for _ in range(c[0])]
for i in range(c[0]):
    for j in range(c[1]):
        if arr[i][j] != brr[i][j]:
            result[i][j] = 1
            print(1, end=" ")
        else:
            result[i][j] = 0
            print(0, end=" ")
    print()