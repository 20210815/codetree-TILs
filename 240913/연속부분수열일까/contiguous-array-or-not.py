arr_ind = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

if b[0] in a:
    ind = a.index(b[0])
    for i in range(ind, arr_ind[0]): # 4 10 4 5 6 /  0 2
        if a[i] != b[i-ind]:
            print("No")
            break
        elif i-ind == len(b)-1:
            print("Yes")
            break
else:
    print("No")