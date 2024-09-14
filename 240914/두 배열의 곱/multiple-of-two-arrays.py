arr = [0] * 3
for i in range(3):
    arr[i] = list(map(int, input().split()))
a = input()
brr = [0] * 3
for i in range(3):
    brr[i] = list(map(int, input().split()))


for i in range(3):
    for j in range(3):
        print(arr[i][j] * brr[i][j], end=" ")
    print()