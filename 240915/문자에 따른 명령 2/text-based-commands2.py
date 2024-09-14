n = input()
# 3 x 1

# 2 
# y
# 4

r = 2
x = 0
y = 0
for i in range(len(n)): #몇 번인지
    if n[i] == 'L':
        r += 1
        r %= 4
    elif n[i] == 'R':
        r -= 1
        r %= 4
    elif n[i] == 'F':
        if r == 1:
            y += 1
        elif r == 2:
            x += 1
        elif r == 3:
            x -= 1
        elif r == 4:
            y -= 1

print(x, y)