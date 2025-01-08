n, k = map(int, input().split())
arr = list(map(int, input().split()))

s = 0
result = 0
# Write your code here!
for i in range(n-k):
    for j in range(k):
        s += arr[i+j]
    if result < s :
        result = s
    s = 0

print(result)