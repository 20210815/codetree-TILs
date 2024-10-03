n = int(input())

arr = [[_ for _ in range(n)] for _ in range(n)]


num = 1
def make_square(n):
    global num
    for i in range(n):
        for j in range(n):
            if num == 10:
                num = 1
                arr[i][j] = num
            else:
                arr[i][j] = num
                num += 1
                
    print_arr(n)

def print_arr(n):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()
#1234
#5678


make_square(n)