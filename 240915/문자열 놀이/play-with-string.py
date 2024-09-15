s = list(map(str, input().split()))
string = list(s[0])
q = int(s[1])

tmp = ''
for i in range(q):
    que = list(map(str, input().split()))
    if int(que[0]) == 1:
        tmp = string[int(que[1])-1]
        string[int(que[1])-1] = string[int(que[2])-1]
        string[int(que[2])-1] = tmp
        for i in string:
            print(i, end="")
    elif int(que[0]) == 2:
        for i in range(len(string)):
            if string[i] == que[1]:
                string[i] = que[2]
            print(string[i], end="")
    print()