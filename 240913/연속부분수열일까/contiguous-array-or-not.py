arr_ind = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))
# 1 5 2 6
# 5 6


# 4 1 3 1 3 1 4


# 9 2 4 1 3 3 1 4 6 8
# 4 1 3 1 3 1 4

cnt = 1
if b[0] in a:
    for i in range(a.index(b[0])+1, len(a)):
        if a[i] == b[cnt]:
            if len(b)-1 ==  cnt:
                print("Yes")
                break
            else:
                cnt += 1
                continue
        else:
            if b[1] in a[i+1:]:
                a[i+1:].index(b[1])
            else:
                print("No")
                break
    
else: 
    print("No")