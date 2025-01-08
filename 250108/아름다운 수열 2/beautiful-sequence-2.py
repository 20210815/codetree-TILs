N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0
# Write your code here!
for i in range(N-M+1):
    for j in range(M):
        if B[j] not in A[i:i+M]:
            break
        else:
            if j == M-1:
                #print(A[i:i+M])
                count += 1
print(count)