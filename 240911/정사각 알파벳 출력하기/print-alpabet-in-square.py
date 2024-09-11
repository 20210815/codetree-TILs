n = int(input())

for i in range(n):
    for j in range(n):
        print(chr(ord('A')+i*n+j), end="")
    print()


# (1,1) (1,2), (1,3) (1,4)
# (2,1) (2,2) (2,3) (2,4)