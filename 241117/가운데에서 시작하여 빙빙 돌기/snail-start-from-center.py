n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def inRange(x1, y1):
    global arr
    if x1 >= 0 and y1 >= 0 and x1 < n and y1 < n and arr[x1][y1] == 0:
        return True
    else:
        return False


x, y = n-1, n-1
dir = 0
for i in range(n*n, 0, -1):
    if i == n*n:
        arr[x][y] = n*n
    else:
        nx , ny = x + dx[dir], y + dy[dir]
        if not inRange(nx, ny):
            dir = (dir+1) %4
        x, y =   x + dx[dir], y + dy[dir]
        arr[x][y] = i

for row in arr:
    print(*row)