n = int(input())

arr = [1, n]

for i in range(2, 20):
    sum = arr[i-1] + arr[i-2]
    arr.append(sum)

    if sum > 100:
        break

for i in range(len(arr)):
    print(arr[i], end=" ")