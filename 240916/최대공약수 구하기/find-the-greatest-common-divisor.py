def 최대공약수(n, m):
    while m != 0:
        n, m = m, n % m
    print(n)

sd = list(map(int, input().split()))
if sd[0] > sd[1]:
    n = sd[0]
    m = sd[1]
else:
    m = sd[0]
    n = sd[1]

최대공약수(n,m)