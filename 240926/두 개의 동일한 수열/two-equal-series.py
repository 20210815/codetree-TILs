n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

for i in range(n):
    if a[i] != b[i]:
        print("No")
        break
    else:
        if n-1 == i:
            print("Yes")