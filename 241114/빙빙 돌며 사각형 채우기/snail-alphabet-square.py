n, m = tuple(map(int, input().split()))

arr = [['' for _ in range(m)] for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def inRange(x1, y1):
    if x1 >= 0 and y1 >= 0 and x1 < n and y1 < m and arr[x1][y1] == '':
        return True
    else:
        return False

dir = 0
x, y = 0, 0
init = 'A'
MAX = 'Z'
for i in range(0, n*m):
    arr[x][y] = init

    nx, ny = x + dx[dir], y + dy[dir]
    if not inRange(nx, ny):
        dir = (dir + 1) % 4
    x, y = x + dx[dir], y + dy[dir]

    if init == 'Z':
            init = 'A'
    else:
        init = chr((ord(init) + 1))


for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()