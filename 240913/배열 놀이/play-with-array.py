nq = list(map(int, input().split()))

arr = list(map(int, input().split()))

for i in range(nq[1]):
    que = list(map(int, input().split()))
    if que[0] == 1:
        print(arr[(que[1]-1)])
    elif que[0] == 2:
        if que[1] in arr:
            print(arr.index(que[1])+1) #몇번째 원소인지
        else:
            print(0)
    else:
        for k in range(que[1]-1, que[2]):
            print(arr[k], end=" ")
        print()