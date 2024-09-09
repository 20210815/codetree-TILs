n = int(input())

for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")

        #if i < 6
    print()

for i in range(1, n+1):
    for j in range(n-i):
        print("*", end=" ")
    print()