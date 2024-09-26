n = int(input())
str_arr = [''] * n

for i in range(n):
    str_arr[i] = input()


str_arr.sort()

for i in range(n):
    print(str_arr[i])