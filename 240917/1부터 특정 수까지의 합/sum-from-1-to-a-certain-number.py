def print_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum // 10


n = int(input())

result = print_sum(n)
print(result)