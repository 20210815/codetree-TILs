string = input()
li = []
cnt = 1
sum = 0
ch = string[0]
if len(string) == 1:
    print(2)
    print(f"{ch}{cnt}", end="")
else:
    for i in range(len(string)-1): #aaabbbbcbb
        if ch == string[i+1]:
            cnt += 1
            if i == len(string)-2:
                li.append([ch, cnt])
        
        else:
            li.append([ch,cnt])
            ch = string[i+1]
            cnt = 1
            if i == len(string)-2:
                li.append([ch, cnt])

    print(len(li)*2)
    for i in range(len(li)):
        for j in range(2):
            print(li[i][j],end="")