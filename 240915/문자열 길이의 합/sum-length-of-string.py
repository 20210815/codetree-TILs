n = int(input())

string = [input() for _ in range(n)]

sum = 0
cnt = 0
for i in range(n):
    sum += len(string[i])
    if string[i][0] == 'a':
        cnt += 1

print(sum, cnt)