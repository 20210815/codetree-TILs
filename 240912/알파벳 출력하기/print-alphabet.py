n = int(input())
cnt = 0
for i in range(n):
    for j in range(i+1):
        print(chr(ord('A')+cnt), end="")
        cnt += 1
        if (ord('A')+cnt > ord('Z')):
            cnt = 0
    print()