n = input()

cnt = 0
cnt1 = 0

for i in range(len(n)):
    if n[i:i+2] == 'ee':
        cnt += 1
    if n[i:i+2] == 'eb':
        cnt1 += 1
print(cnt, cnt1)