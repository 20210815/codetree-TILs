n = int(input())

for i in range(n, 0, -1): # 여기가 행 세어주는 곳
    for j in range(i): # 별 그려주는 곳
        print("*", end=" ")
    print()