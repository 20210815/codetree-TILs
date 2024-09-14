n = list(map(int, input().split()))

arr = [[0 for _ in range(n[1])] for _ in range(n[0])]

# (0,0) / (0,1) (1,0) / (0,2) (1,1) (2,0) / (2,1) (1,2) / (2,2)
# 
# 4 5 6 4
# 3,3 = 4 3
# 1,6 = 6 1 * 6
# 4, 4 = 9
cnt = 1
if n[0] == 1 or n[1] == 1:
    for i in range(n[0] * n[1]):
        for j in range(n[0]):
            if i - j < 0:
                continue
            elif i - j >= n[1]:
                continue
            else:
                arr[j][i-j] = cnt
                cnt += 1
                #print(f"{i}({j}, {i-j})")
else:
    for i in range((n[0]-1)*(n[1]-1)+1):
        #print(i)
        for j in range(n[0]):
            if i - j < 0:
                continue
            elif i - j == n[1]:
                continue
            else:
                arr[j][i-j] = cnt
                cnt += 1
                #print(f"{i}({j}, {i-j})")

for i in range(n[0]):
    for j in range(n[1]):
        print(arr[i][j], end=" ")
    print()