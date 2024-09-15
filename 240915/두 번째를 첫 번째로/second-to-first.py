n = list(input())

ch = n[0]
ch1 = n[1]
for i in range(len(n)):
    if ch1 == n[i]:
        n[i] = ch
    print(n[i], end="")