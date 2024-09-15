n = input()

n = list(n)

n[1] = 'a'
n[-2] = 'a'

for i in n:
    print(i, end="")