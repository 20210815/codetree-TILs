N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0
# Write your code here!
for i in range(N-M+1):
    if set(B) == set(A[i:i+M]):
        count+=1

print(count)