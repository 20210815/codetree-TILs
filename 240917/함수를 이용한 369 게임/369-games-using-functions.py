def check_3(a, b):
    cnt = 0
    for i in range(a, b+1):
        if i % 3 == 0 or (check_369(i) == True):
            cnt += 1
    return cnt

def check_369(i):
    if i > 1000000:
        if i // 1000000 == 3 or i // 1000000 == 6 or i // 1000000 == 9:
            return True
        else:
            i %= 1000000


    if i > 100000:
        if i // 100000 == 3 or i // 100000 == 6 or i // 100000 == 9:
            return True
        else:
            i %= 100000

    
    if i > 10000:
        if i // 10000 == 3 or i // 10000 == 6 or i // 10000 == 9:
            return True
        else:
            i %= 10000


    if i > 1000:
        if i // 1000 == 3 or i // 1000 == 6 or i // 1000 == 9:
            return True
        else:
            i %= 1000

    if i > 100:
        if i // 100 == 3 or i // 100 == 6 or i // 100 == 9:
            return True
        else:
            i %= 100
            
    if i > 10:
        if i // 10 == 3 or i // 10 == 6 or i // 10 == 9:
            return True
        else:
            i %= 10
    if i > 1:
        if i == 3 or i == 6 or i == 9:
            return True
        else:
            return False

a, b = tuple(map(int, input().split()))
result = check_3(a, b)
print(result)