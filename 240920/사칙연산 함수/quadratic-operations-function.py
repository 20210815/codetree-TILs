def plus(a, c):
    return a + c

def minus(a, c):
    return a- c

def multi(a, c):
    return a * c

def divi(a, c):
    return a // c

a, o, c = list(map(str, input().split()))

result = 0
if o == '+':
    print(f"{a} {o} {c} = {plus(int(a), int(c))}")
elif o == '-':
    print(f"{a} {o} {c} = {minus(int(a), int(c))}")
elif o == '*':
    print(f"{a} {o} {c} = {multi(int(a),int(c))}")
elif o == '/':
    print(f"{a} {o} {c} = {divi(int(a), int(c))}")
else:
    print("False")