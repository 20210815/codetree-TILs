arr = list(map(int, input().split()))
a = arr[0]
b = arr[1]

for i in range(a, b+1):
    if 1920 % i == 0 and 2880 % i == 0:
        print("1")
        break
    else:
        if i == b:
            print("0")