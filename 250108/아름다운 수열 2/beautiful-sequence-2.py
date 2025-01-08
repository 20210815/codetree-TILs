N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0
# Write your code here!
for i in range(N-M+1):
    arr = A[i:i+M]
    arr.sort()
    B.sort()
    for j in range(M):
        if arr[j] != B[j]:
            break
        else:
            if j == M-1:
                count+=1


print(count)