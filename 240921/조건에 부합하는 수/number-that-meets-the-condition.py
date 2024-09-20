a = int(input())

for i in range(1, a):
    if i % 2 == 0 and i % 4 != 0:
        print(i)
    elif (i // 8) % 2 == 0:
        print(i)
    elif i % 7 < 4:
        print(i)
    else:
        continue