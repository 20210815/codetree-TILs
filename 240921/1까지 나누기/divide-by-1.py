n = int(input())

cnt = 0
i = 1
while True:
    if n // i > 1:
        n //= i
        cnt += 1
    else:
        break
    i += 1
print(cnt)