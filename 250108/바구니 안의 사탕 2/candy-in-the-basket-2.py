N, K = map(int, input().split())
arr = [0] * 1000

for _ in range(N):
    candy, pos = tuple(map(int, input().split()))
    arr[pos] += candy

s = 0
result = 0
for i in range(len(arr)-(K*2)):
    s = sum(arr[i:i+(K*2)+1])
    if result < s:
        result = s
    s = 0

print(result)