n = int(input())

# 1      1
# 4 4         n 
# 2      3    3 - 1 = 2
# 3 3         n - cnt 
# 3      5    5 - 2 = 3
# 2 2         n - cnt
# 4      7    7 - 3 = 4
# 1 1         8 - 7

cnt = 0

for i in range(1, n*2+1):
    if (i % 2 == 1):
        for j in range(i - cnt):
            print("*", end=" ")
        
    else :
        for k in range(n - cnt):
            print("*", end=" ")
        cnt = cnt + 1
    print()