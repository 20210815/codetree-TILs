N, B = tuple(map(int, input().split()))

change = []
num = 0

while (True):
    if N < B :
        change.append(N)
        break
    change.append(N % B)
    N = N // B

for k in range(len(change)-1, -1, -1):
    print(change[k], end="")