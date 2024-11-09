a, b = map(int, input().split())


gcd = 0
for i in range(a, b):
    if 1920 % i == 0 and 2880 % i == 0:
        gcd = i

if gcd != 0:
    print(1)
else:
    print(0)