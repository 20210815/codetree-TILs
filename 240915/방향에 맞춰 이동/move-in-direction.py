n = int(input())

x= 0
y= 0
for i in range(n):
    an = list(map(str, input().split()))
    if an[0] == 'W':
        x -= int(an[1])
    elif an[0] == 'S':
        y -= int(an[1])
    elif an[0] == 'N':
        y += int(an[1])
    elif an[0] == 'E':
        x += int(an[1])
    #print(x, y)

print(x, y)