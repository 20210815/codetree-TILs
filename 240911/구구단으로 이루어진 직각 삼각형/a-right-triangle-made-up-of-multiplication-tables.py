n = int(input())

for i in range(0, n):
    for j in range(1, n-i+1):
        if j == n-i:
            print(f"{i+1} * {j} = {(i+1)*j}", end="")
        else:
            print(f"{i+1} * {j} = {(i+1)*j}", end=" / ")
    print()