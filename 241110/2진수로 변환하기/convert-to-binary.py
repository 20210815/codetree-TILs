n = int(input())

binary = []

while(True):
    if n < 2:
        binary.append(n)
        break
    else:
        binary.append(n % 2)
        n = n // 2

for b in binary[::-1]:
    print(b, end="")