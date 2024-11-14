N = int(input())

A = list(map(int, input().split()))

result = 0

# 순서 만족하기 위해서는 i 제외
for i in range(N):
    for j in range(i, N):
        for k in range(j, N):
            if i < j and j < k: #위치가 i < j < k 면서
            # 키도 i <= j <= k
                if A[i] <= A[j] and A[j] <= A[k]:
                    result += 1
print(result) 