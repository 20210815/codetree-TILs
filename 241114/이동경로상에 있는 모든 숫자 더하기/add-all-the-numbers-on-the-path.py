N, T = tuple(map(int, input().split()))

cmd = input()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

arr = [[i * 3 +j + 1 for j in range(N)] for i in range(N)]

def inRange(x1, y1):
    if x1 >= 0 and y1 >= 0 and x1 < N and y1 < N:
        return True
    else:
        return False

dir = 0
x, y = N//2, N//2
result = arr[x][y]

#print(x, y)
for test in cmd:
    if test == 'L':
        dir = (dir - 1) %4
    
    elif test == 'R':
        dir = (dir + 1) % 4
    else:
        nx, ny = x + dx[dir], y + dy[dir]
        if inRange(nx, ny):
            x, y = x + dx[dir], y + dy[dir]
            #print(arr[x][y])
            result += arr[x][y]
        else:
            pass

print(result)


