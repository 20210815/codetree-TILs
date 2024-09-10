n = int(input())

# n =2
# 출력 5
# 출력 1 공백 1 출력 1 공백 1 출력 1

for i in range(n * 2 + 1):
    if (i % 2 == 0):
        for _ in range(n * 2 + 1):
            print("*", end=" ")
        print()
    else :
        for _ in range(n + 1):
            print("*", end=" ")
            print(" ", end=" ")
        print()