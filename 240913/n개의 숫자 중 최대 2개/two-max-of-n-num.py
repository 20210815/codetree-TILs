import sys
n = int(input())

arr = list(map(int, input().split()))

sort1 = [0] * n

arr.sort(reverse=True)

print(arr[0], arr[1])