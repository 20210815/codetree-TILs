n = int(input())

arr = list(map(int, input().split()))

max_index = 0
max_val = arr[0]

while True:
        for i in range(n):
            if max_val == arr[i]:
                if i == n-1 :
                    print(max_index+1, end=" ")
                    break
                else:
                    pass
            elif max_val < arr[i]:
                max_val = arr[i]
                max_index = i
                arr[i] = 0
                print(max_index+1, end=" ")
                if max_index +1 == 1 :
                    break
        if max_index +1 == 1:
            break
        max_val = 0
        max_index = 0