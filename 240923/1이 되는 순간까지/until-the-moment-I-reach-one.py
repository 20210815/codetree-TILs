def count_sum(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return count_sum(n // 2) + 1
    else:
        return count_sum(n // 3) + 1
    
n = int(input())
print(count_sum(n))