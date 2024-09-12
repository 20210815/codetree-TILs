n = int(input())

arr = list(map(int, input().split()))

arr_new = [elem ** 2 for elem in arr]

for i in range(len(arr_new)):
    print(arr_new[i], end=" ")