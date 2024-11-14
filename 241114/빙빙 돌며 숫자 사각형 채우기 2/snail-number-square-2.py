dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = tuple(map(int, input().split()))

arr = [[0 for _ in range(m)] for _ in range(n)]


def inRange(x1, y1):
    if x1 >= 0 and y1 >= 0 and x1 < n and y1 < m and arr[x1][y1] == 0:
        return True
    else:
        return False

dir = 0
x, y = 0, 0
for i in range(1, (n * m)+1):
    #print(x, y)
    arr[x][y] = i
    nx, ny = x + dx[dir], y + dy[dir]
    if not inRange(nx, ny):
        dir = (dir + 1) % 4
    x, y = x + dx[dir], y + dy[dir]
    
    

for i in range(n):
    for j in range(m):
        print(arr[i][j], end= " ")
    print()