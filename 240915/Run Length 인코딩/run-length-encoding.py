string = input()
li = []
cnt = 1
sum = 0
ch = string[0]
for i in range(len(string)-1): #aaabbbbcbb
    if ch == string[i+1]:
        cnt += 1
        if i+1 == len(string)-1:
            li.append([ch, cnt])
        
    else:
        li.append([ch,cnt])
        ch = string[i+1]
        cnt = 1

print(len(li)*2)
for i in range(len(li)):
    for j in range(2):
        print(li[i][j],end="")