a, b = tuple(map(int, input().split()))

n = list(input())

num = 0
# n은 a진수
for i in n:
    num = num * a + int(i)

change = []
while True:
    if num < b:
        change.append(num)
        break
    change.append(num % b)
    num = num // b


for i in change[::-1]:
    print(i, end="")