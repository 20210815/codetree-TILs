n = list(map(str, input().split()))

if len(n[0]) > len(n[1]):
    print(n[0], len(n[0]))
elif len(n[1]) > len(n[0]):
    print(n[1], len(n[1]))
else:
    print("same")