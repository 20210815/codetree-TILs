n, k, T = tuple(map(str, input().split()))

stri = []

for i in range(int(n)):
    s = input()
    if s[:len(T)] == T:
        stri.append(s)

stri.sort()

print(stri[int(k)-1])