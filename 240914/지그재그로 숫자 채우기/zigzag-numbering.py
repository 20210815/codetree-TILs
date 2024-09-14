n = list(map(int, input().split()))
# n[0] 행, n[1] 열

arr = [[0 for _ in range(n[1])] for _ in range(n[0])]

# 0 (4*i(4-0)-1)7 8 15
# 1 6 9 14
# 2 5 10 13
# 3 4 11 12
for i in range(n[1]): #6
    for j in range(n[0]): #4
        if i % 2 == 0:
            arr[j][i] = i * n[0] + j
        else:
            arr[j][i] = n[0] * i + (n[0] - j - 1)

for i in range(n[0]):
    for j in range(n[1]):
        print(arr[i][j], end=" ")
    print()