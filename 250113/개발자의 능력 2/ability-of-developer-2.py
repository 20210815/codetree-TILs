import sys

ability = list(map(int, input().split()))
INT_MAX = sys.maxsize
n = 6
# Write your code here!

def diff(i, j , k, l):
    sum1 = ability[i] + ability[j]
    sum2 = ability[k] + ability[l]
    sum3 = sum(ability) - sum1 - sum2

    ret = abs(sum1 - sum2)
    ret = max(ret, abs(sum2-sum3))
    ret = max(ret, abs(sum3-sum1))
    return ret

min_diff = INT_MAX
for i in range(n):
    for j in range(i+1, n):

        #두번째 팀원
        for k in range(n):
            for l in range(k+1, n):
                if k == i or k == j or k == l or l == j:
                    continue
                min_diff = min(min_diff, diff(i,j ,k, l))

print(min_diff)