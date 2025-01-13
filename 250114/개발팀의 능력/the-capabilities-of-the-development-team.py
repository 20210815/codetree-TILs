import sys
arr = list(map(int, input().split()))
n = 5
min_diff = sys.maxsize
# Write your code here!

def diff(i, j , k , l):
    sum1 = arr[i] + arr[j]
    sum2 = arr[k] + arr[l]
    sum3 = sum(arr) - sum2 - sum1
    if sum1 == sum2 and sum2 == sum3:
        return sys.maxsize

    ret = abs(sum1- sum2)
    ret = max(ret, abs(sum2- sum3))
    ret = max(ret, abs(sum3 - sum1))
    return ret



for i in range(n):
    for j in range(i+1, n):

        for k in range(n):
            for l in range(k+1, n):
                if k == i or k == j or l == i or l == j:
                    continue
                min_diff = min(min_diff, diff(i, j, k, l))

print(min_diff)