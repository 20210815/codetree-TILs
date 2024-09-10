n = int(input())

for i in range(n):
    for j in range(n):
        # 홀수열 순서대로
        if j % 2 == 0:
            print(i+1, end="")

        # 짝수열 반대로
        else:
            print(n-i, end="")
    print()