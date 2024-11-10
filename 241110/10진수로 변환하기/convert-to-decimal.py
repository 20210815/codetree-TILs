binary = list(input())
num = 0

for i in range(1, len(binary)):
    num = num * 2 + binary[i]

print(num)