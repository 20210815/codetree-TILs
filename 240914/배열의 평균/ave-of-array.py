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

a = sum(arr[0])
b = sum(arr[1])
print((a+b)/8, end=" ")