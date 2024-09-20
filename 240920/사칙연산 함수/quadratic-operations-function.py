def plus(a, c):
    return a + c

def minus(a, c):
    return c - a

def multi(a, c):
    return a * c

def divi(a, c):
    return c // a

a, o, c = list(map(str, input().split()))

result = 0
if o == '+':
    result = plus(int(a), int(c))
    print(f"{a} {o} {c} = {result}")
elif o == '-':
    result = minus(int(a), int(c))
    print(f"{a} {o} {c} = {result}")
elif o == '*':
    result = multi(int(a),int(c))
    print(f"{a} {o} {c} = {result}")
elif o == '/':
    result = divi(int(a), int(c))
    print(f"{a} {o} {c} = {result}")
else:
    print("False")