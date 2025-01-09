N = int(input())
a, b, c = map(int, input().split())

result = 0

# Write your code here!
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if abs(k-c) <= 2 or abs(j-b) <= 2 or abs(i-a) <= 2:
                result += 1
            else:
                break

print(result)