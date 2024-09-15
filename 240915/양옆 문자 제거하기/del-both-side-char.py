n = list(input())

n.pop(2)
n.pop(-2)

for i in range(len(n)):
    print(n[i],end="")