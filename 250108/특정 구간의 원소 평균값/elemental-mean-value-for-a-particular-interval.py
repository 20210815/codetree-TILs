n = int(input())
arr = list(map(int, input().split()))

count = 0
# Write your code here!
for i in range(n):
    for j in range(i, n):
        avgN = sum(arr[i:j+1])/(j-i+1)
        #print(avgN)
        #print(arr[j])
        for k in range(i, j+1, 1):
            if avgN == arr[k]:
                count += 1
                break

print(count)