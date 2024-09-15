n = input()

ch = n[0]
ch1 = n[1]

for i in n:
    if ch == i:
        i = ch1
    elif ch1 == i:
        i = ch
    print(i, end="")