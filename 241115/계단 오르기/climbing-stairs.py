MAX = 1000
MOD = 10007

dp = [0] * (MAX+1)

dp[0] = 1
dp[1] = 0
dp[2] = 1
dp[3] = 1


n = int(input())
for i in range(4, n+1):
    dp[i] = (dp[i - 2] + dp[i - 3]) % MOD

print(dp[n])