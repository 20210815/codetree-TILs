n = input()
ch = input()

for i in range(len(n)):
    if n[i:i+len(ch)] == ch:
        print(i)
    else:
        if i == len(n):
            print(-1)