init = input()

sp = init.split()

a = int(sp[0])
b = int(sp[1])

for i in range(2, 9, 2):
    for j in range(b, a-1, -1):
        print(f"{j} * {i} = {j*i}", end="")
        if j > a:
            print("", end=" / ")
    print()