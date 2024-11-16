N, M = tuple(map(int, input().split()))

arr = [[0 for _ in range(N+1)] for _ in range(N+1)]


for _ in range(M):
    x, y = tuple(map(int, input().split()))
    arr[x][y] = 1
    arr[y][x] = 1

cnt = 0
visited = [False for _ in range(N+1)]

def dfs(vertex):
    global cnt
    for v in range(1,N+1):
        if arr[vertex][v] and not visited[v]:
            visited[v] = True
            cnt += 1
            dfs(v)

visited[1] = True
dfs(1)

print(cnt)