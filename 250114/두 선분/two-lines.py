x1, x2, x3, x4 = map(int, input().split())

# Write your code here!
line = [0] * 100000


for i in range(x1, x2+1):
    line[i] += 1

for i in range(x3, x4+1):
    line[i] += 1

for i in range(len(line)):
    if line[i] >= 2:
        print('intersecting')
        break
    else:
        if i == len(line) -1:
            print('nonintersecting')