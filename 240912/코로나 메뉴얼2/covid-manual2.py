arr = [0] * 4
for i in range(3):
    init = input().split()
    if init[0] == 'Y' and int(init[1]) >= 37:
        arr[0] += 1
    elif init[0] == 'N' and int(init[1]) >= 37:
        arr[1] += 1
    elif init[0] == 'Y' and int(init[1]) < 37:
        arr[2] += 1
    else:
        arr[3] += 1
    
for i in range(4):
    print(arr[i], end=" ")

if arr[0] >= 2:
    print("E", end=" ")