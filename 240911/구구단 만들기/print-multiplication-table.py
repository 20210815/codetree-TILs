init = input()

sp = init.split()
a = int(sp[0])
b = int(sp[1])

for i in range(1, 10):
    for j in range(b, a-1, -2):
        print(f"{j} * {i} = {i*j}", end="")
        if j > a:
            print("", end=" / ")
    print()