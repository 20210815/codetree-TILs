n = int(input())

if n % 2 == 1:
    n += 3
    if n % 3 == 0:
        print("%d" %(n//3))
    else:
        print(n)
else:
    if n % 3 == 0:
        print("%d" %(n//3))
    else:
        print(n)