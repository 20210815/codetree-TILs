a, b = tuple(map(int, input().split()))

def calu(a, b):
    if a > b:
        b += 10
        a *= 2
    else:
        a += 10
        b *= 2
    return a, b

a, b = calu(a,b)
print(a, b)