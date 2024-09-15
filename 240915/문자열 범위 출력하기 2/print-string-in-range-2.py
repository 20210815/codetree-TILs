string = input()
n = int(input())

cnt = 0
for i in range(len(string)-1, -1, -1):
    if cnt < 11:
        print(string[i], end="")
        cnt += 1