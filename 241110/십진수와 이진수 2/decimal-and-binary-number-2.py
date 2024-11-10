N = list(input())

num = 0 
for i in N:
    num = num * 2 + int(i)

num *= 17

binary = []
while True:
    if num < 2:
        binary.append(num)
        break
    binary.append(num % 2)
    num = num // 2


for i in range(len(binary)-1, -1, -1):
    print(binary[i], end="")