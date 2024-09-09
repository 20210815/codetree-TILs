n = int(input())

for i in range(1, n+1):                   #1:1 2:3 3:5 4:7
    for j in range(i * 2 - 1):
        print("*", end="")
    print()