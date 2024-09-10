ab = input()

sp = ab.split()

a = int(sp[0])
b = int(sp[1])

for i in range(1, a+1):
    for j in range(i, (b+1)*i, i):
        print(j, end=" ")
    print()