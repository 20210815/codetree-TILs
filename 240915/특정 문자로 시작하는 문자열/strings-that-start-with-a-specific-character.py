n = int(input())

string = [''] * n

sum = 0
for i in range(n):
    string[i] = input()

ch = input()

cnt = 0
for i in range(n):
    if ch == string[i][0]:
        cnt += 1
        sum += len(string[i])

print("%d %.2f" %(cnt, sum/cnt))