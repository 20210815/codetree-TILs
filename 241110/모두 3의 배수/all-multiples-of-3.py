for i in range(5):
    a = int(input())
    if a % 3 != 0:
        print(0)
        break
    else:
        if i == 5:
            print(1)
        else:
            print(0)
            break