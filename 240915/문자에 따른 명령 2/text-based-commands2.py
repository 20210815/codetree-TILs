n = input()
# 3 x 1

#   2 
# 3 y 1
#   4

r = 2
x = 0
y = 0
for i in range(len(n)): #몇 번인지
    if n[i] == 'L':
        if r == 4:
            r = 1
        else :
            r += 1
    elif n[i] == 'R':
        if r == 1:
            r = 4
        else:
            r -= 1
    elif n[i] == 'F':
        if r == 1:
            x += 1
        elif r == 2:
            y += 1
        elif r == 3:
            x -= 1
        elif r == 4:
            y -= 1

print(x, y)