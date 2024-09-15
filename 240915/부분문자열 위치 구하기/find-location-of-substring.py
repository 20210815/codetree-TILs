n = input()
ch = input()

for i in range(len(n)):
    if n[i:i+len(ch)] == ch:
        print(i)
        break
    else:
        if i == len(n)-1:
            print(-1)