n = input()

for i in range(len(n)-1, -1, -1):
    if i % 2 == 1:
        print(n[i],end="")