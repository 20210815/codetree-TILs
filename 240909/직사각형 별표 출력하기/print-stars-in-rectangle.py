init = input()

sp = init.split()
n = int(sp[0])
m = int(sp[1])

for i in range(n):
    for j in range(m):
        print("*", end=" ")
    print()