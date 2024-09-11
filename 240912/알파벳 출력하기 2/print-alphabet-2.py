n = int(input())

cnt = 0

for i in range(n):
    for j in range(i):
        print(" ", end="")
    for k in range(n-i):
        print("2", end=" ")
    print()