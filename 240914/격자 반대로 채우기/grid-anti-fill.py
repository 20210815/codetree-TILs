n = int(input())

# (3,3) (2,3) (1,3) (0,3)
# (0,2) (1,2) (2,2) (3,2)
# 3 2 1 0 

# 1 7 차이

arr = [[0 for _ in range(n)] for _ in range(n)]


cnt = 1
line = 1
#n-1이 무조건 거꾸로
for i in range(n-1, -1, -1):
    if line % 2 == 1:
        for j in range(n-1, -1, -1):
            arr[j][i] = cnt
            cnt += 1
    else:
        for j in range(n):
            arr[j][i] = cnt
            cnt += 1
    line += 1
    
for i in range(n):
    for j in range(n):
        print(arr[i][j], end= " ")
    print()