n = int(input())

arr = [[_ for _ in range(n)] for _ in range(n)]

def make_square(n):
    for i in range(n):
        for j in range(n):
            if i * n + j + 1 <= (n*2+1):
                arr[i][j] = i * n + j + 1
            else:
                arr[i][j] = i * n + j + 1 - 9
    print_arr(n)

def print_arr(n):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()
#1234
#5678


make_square(n)