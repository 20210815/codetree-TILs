arr = list(map(int, input().split()))

new_arr=[]
for i in range(len(arr)):
    if arr[i] < 250:
        new_arr.append(arr[i])
    else:
        break

print("%d %.1f" %(sum(new_arr), sum(new_arr)/len(new_arr)))