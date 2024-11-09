a, b = map(int, input().split())


gcd = 0
for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        gcd = i

if gcd != 0:
    print(1)
else:
    print(0)