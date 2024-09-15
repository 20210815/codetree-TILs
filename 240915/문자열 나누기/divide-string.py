n = int(input())

string = list(map(str, input().split()))

result = []
for i in range(n):
    result += string[i]

for i in range(len(result)):
    print(result[i], end="")
    if i % 5 == 4:
        print()