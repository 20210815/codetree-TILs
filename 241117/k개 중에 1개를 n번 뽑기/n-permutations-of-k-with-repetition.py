K, N = tuple(map(int, input().split()))

def dfs(n):
    global arr
    if n == N+1:
        print(arr)
        return
    for i in range(1, K+1):
        arr.append(i)
        dfs(n+1)
        arr.pop()


arr = []
dfs(1)