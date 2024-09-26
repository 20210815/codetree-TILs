n = int(input())

a = list(map(int, input().split()))

li = []
max = 0
cnt = 0
for i in range(len(a)):
    if cnt != n:
        li.append(a[i])
        cnt += 1
    else:
        if max < sum(li):
            max += sum(li)
            cnt = 0
            li.clear()

print(max)