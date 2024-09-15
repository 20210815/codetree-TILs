n = list(map(str, input().split()))

if n[1] in n[0]:
    print(n[0].index(n[1]))
else:
    print("No")