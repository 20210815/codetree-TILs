n = int(input())

# n=3
# 별 1:1 2:3 3:5 1:3 2:1 (n-i)* 2 -1
#공백1:2 2:1 3:0 1:1 2:2

for i in range(1, n+1):
    for k in range(n-i):
        print(" ", end="")
    for j in range(i * 2 - 1):
        print("*", end="")
    print()

for i in range(1, n):
    for k in range(i):
        print(" ", end="")
    for j in range((n-i)* 2 -1):
        print("*", end="")
    print()