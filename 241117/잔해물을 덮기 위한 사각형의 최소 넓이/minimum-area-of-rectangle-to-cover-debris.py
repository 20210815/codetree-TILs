OFFSET = 100
MAX = 200

def checkingList(x1, x2, y1, y2, k):
    global arr
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i+OFFSET][j+OFFSET] = k

x1, y1, x2, y2 = tuple(map(int, input().split()))

rx1, ry1, rx2, ry2 = tuple(map(int, input().split()))

arr = [[0 for _ in range(MAX)] for _ in range(MAX)]

checkingList(x1, x2, y1, y2, 1)
checkingList(rx1, rx2, ry1, ry2, 2)

min_x, min_y = MAX, MAX
max_x, max_y = 0, 0
for i in range(MAX):
    if arr[i].count(1) >= 1:
        for j in range(MAX):
            if arr[i][j] == 1:
                min_x = min(i, min_x)
                min_y = min(j, min_y)
                max_x = max(i,max_x)
                max_y = max(j, max_y)

print((max_x-min_x+1) * (max_y - min_y+1))