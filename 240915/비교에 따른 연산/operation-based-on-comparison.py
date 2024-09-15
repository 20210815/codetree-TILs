nm = list(map(int, input().split()))
a= nm[0]
b = nm[1]

if a > b:
    print(a*b)
else:
    print(b//a)