n = int(input())

arr = list(map(int, input().split()))

in_list = []
for i in range(n):
    if arr.count(arr[i]) == 1:
        in_list.append(arr[i])
    elif i == n-1 and len(in_list) == 0:
        print(-1)

if len(in_list) != 0: 
        max_val = in_list[0]
        for j in range(1, len(in_list)):
            if max_val < in_list[j]:
                max_val = in_list[j]
            print(max_val)