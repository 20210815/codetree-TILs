arr = list(map(int,input().split()))

modu = [0] * 10
while True:
    if arr[0] <= 1:
        break
    else:
        result = arr[0] % arr[1]
        modu[result] += 1
        arr[0] = arr[0] // arr[1]
sum = 0
for i in range(len(modu)):
    sum += modu[i] **2

print(sum)