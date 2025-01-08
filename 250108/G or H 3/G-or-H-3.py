n, k = map(int, input().split())
arr = [] * 100


def sumGH(word):
    if word == 'G':
        return 1
    elif word == 'H':
        return 2

for i in range(n):
    index, alpha = tuple(input().split())
    arr.append((int(index), alpha))

arr.sort()
s = 0
result = 0

for i in range(n):
    for j in range(i, n):
         if arr[i][0] + k >= arr[j][0]:
            s += sumGH(arr[j][1])
    if result < s:
        result = s
    s = 0

print(result)

