arr = [0] * 2

for i in range(2):
    arr[i] = list(map(int, input().split()))
    print(sum(arr[i])/len(arr[i]), end=" ")
print()

a = 0
b = 0
for i in range(4):
    a = arr[0][i]
    b = arr[1][i]
    print((a+b)/2, end=" ")
print()

sum = 0
for i in range(2):
    for j in range(4):
        sum += arr[i][j]
print("%.lf" %(sum/8), end=" ")