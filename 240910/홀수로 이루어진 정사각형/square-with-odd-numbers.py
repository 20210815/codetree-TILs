n = int(input())
s = 11
for i in range(n):
    for j in range(s, s+(n*2), 2):
        print(j, end=" ")
    s += 2
    print()