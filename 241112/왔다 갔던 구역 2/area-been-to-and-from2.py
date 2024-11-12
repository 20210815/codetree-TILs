OFFSET = 1000
MAX = 2000
segment = []
cur = 0
n = int(input())

for i in range(n):
    x, D = tuple(map(str, input().split()))
    x = int(x)
    if D == "L":
       #왼쪽
       seg_L = cur - x
       #오른쪽
       seg_R = cur
       #현재위치 
       cur -= x
    else:
       #왼쪽
       seg_L = cur
       #오른쪽
       seg_R = cur + x
       #현재위치 
       cur += x
    segment.append([seg_L, seg_R])

checked = [0] * (MAX + 1)

for x1, x2 in segment:
    index1, index2 = x1 + OFFSET, x2 + OFFSET
    for i in range(index1, index2):
        checked[i] += 1


result = 0
for ele in checked:
    if ele >= 2:
        result += 1

print(result)