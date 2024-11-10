N, K = tuple(map(int, input().split()))


#n 개의 칸
arr = [0] * (N + 1)

for i in range(K):
    s, e = tuple(map(int, input().split()))
    for j in range(s, e+1):
        arr[j] += 1

print((max(arr)))