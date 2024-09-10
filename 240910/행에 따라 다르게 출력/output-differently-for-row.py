n = int(input())


cnt = 0
for i in range(n):
    if i % 2 == 0:
        for j in range(1, n+1):
            print(j+(cnt*n), end=" ")
        cnt += 1
        print()
    else:
        for k in range(2, n*2+1, +2):
            print(k + (cnt*n), end=" ")
        cnt += 2    
        print()
    


# 1 (4*0)+1 (4*0)+4 => 1
# 2 (4*1)+2 (4*1)+(2*4) => 2
# 3 (4*1)+(2*4)+1 (4*3)+1+4 => 1
# 4 (4*4)+2 (4*4)+(2*4) => 2