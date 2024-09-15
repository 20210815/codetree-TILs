h1 = list(map(str, input().split()))
h2 = list(map(str, input().split()))

if (int(h1[0]) >= 19 and h1[1] == 'M') or (int(h2[0]) >= 19 and h2[1] == 'M'):
    print("1")
else:
    print("0")