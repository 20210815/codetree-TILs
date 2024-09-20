a, b = tuple(map(int, input().split()))

def multi(a, b):
    result = 1
    for i in range(b):
        result *= a
    return result

result = multi(a,b)

print(result)