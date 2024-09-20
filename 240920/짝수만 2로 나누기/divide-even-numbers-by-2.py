n = int(input())

arr = list(map(int, input().split()))

def division2(li, n):
    for i in range(n):
        if li[i] % 2 == 0:
            li[i] //= 2

division2(arr ,n)
for i in range(n):
    print(arr[i], end=" ")