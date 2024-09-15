def make_square(n, m):
    for i in range(n):
        for j in range(m):
            print("1", end="")
        print()

arr = list(map(int, input().split()))
make_square(arr[0], arr[1])