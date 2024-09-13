n = int(input())

arr = list(map(int,input().split()))

# 최댓값의 위치 구하기
# 그 중 제일 왼쪽
while True:
    max_val = arr[0]
    max_ind = 0
    for i in range(n):    
        if max_val == arr[i] and max_ind == i:
            pass
        elif max_val == arr[i] and i > max_ind:
            print(max_ind+1, end=" ")
        elif max_val < arr[i]:
            max_val = arr[i]
            max_ind = i
            print(max_ind+1, end=" ")
            arr[i] = 0
    if max_ind == 0:
        break