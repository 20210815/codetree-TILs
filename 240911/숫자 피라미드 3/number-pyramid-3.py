n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        if i < j:
            continue
        else:
            print(f"{i*j}", end=" ")
    print()