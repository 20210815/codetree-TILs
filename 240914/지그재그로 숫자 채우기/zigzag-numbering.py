n = list(map(int, input().split()))

arr = [[0 for _ in range(n[1])] for _ in range(n[0])]

k = 0
for i in range(n[1]): #열
    if i % 2 == 0:
        for j in range(n[0]):
            arr[j][i] = i * n[0] + j
    else:
        for j in range(n[0]-1, -1, -1):
            arr[k][i] = i * n[0] + j
            k += 1
            
for i in range(n[0]):
    for j in range(n[1]):
        print(arr[i][j], end=" ")
    print()