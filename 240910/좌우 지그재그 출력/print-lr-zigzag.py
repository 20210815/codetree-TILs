n = int(input())

for i in range(0, n):
    if i % 2 == 0:
        for j in range(1, n+1):
            print(j + (n * i), end=" ")
        print()
    else:
        for j in range(n, 0, -1):
            print(j + (n * i), end=" ")
        print()