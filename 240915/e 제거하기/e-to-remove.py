n = list(input())

for i in range(len(n)):
    if n[i] == 'e':
        n.pop(i)
        break

for i in range(len(n)):
    print(n[i], end="")