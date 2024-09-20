a, b = tuple(map(int, input().split()))

def check_num(a, b):
    cnt = 0
    for i in range(a, b+1):
        if oddsum(i) % 2 == 0 and thtn(i):
            cnt += 1
    return cnt

def oddsum(i):
    sum = 0
    while True:
        if i // 10 == 0:
            sum += i % 10
            break
        else:
            sum += i % 10
            i //= 10
    
    return sum


def thtn(i):
    for j in range(2, i):
        if i % j == 0:
            return False
        else:
            if j == i-1:
                return True

print(check_num(a, b))