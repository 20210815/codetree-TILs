n = int(input())

arr = list(map(int, input().split()))

mid = 0
for i in range(0,n,2):
    print(sorted(arr[:i+1])[i//2], end=" ")
    #print(arr[:i+1])


# 0 1 2 3 4 5
# 1 2 3 4 5 6