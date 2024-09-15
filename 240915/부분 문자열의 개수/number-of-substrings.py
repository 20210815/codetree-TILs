n = input()
ch= input()

cnt = 0
for i in range(len(n)):
    if n[i:i+len(ch)] == ch:
        cnt += 1

print(cnt)