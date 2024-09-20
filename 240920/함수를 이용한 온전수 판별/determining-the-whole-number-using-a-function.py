a, b = tuple(map(int, input().split()))

def check_num(a, b):
    cnt = 0
    for i in range(a, b+1):
        if i % 2 != 0:
            if i % 10 != 5:
                if i % 3 == 0 and i % 9 != 0:
                    continue
                else:
                    #print(i)
                    cnt += 1
            else:
                continue
        else:
            continue
    return cnt

print(check_num(a, b))