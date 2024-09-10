n = int(input())

# 공백 2 출력 1
# 공백 1 출력 2
# 공백 0 출력 3
# 공백 0 출력 2
# 공백 0 출력 1

for i in range(1, n+1):
    for k in range(n-i):
        print(" ", end=" ")
    for j in range(i):
        print("@", end=" ")
    print()

for i in range(1, n+1):
    for j in range(n - i):
        print("@", end=" ")
    print()