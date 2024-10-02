a = input()
b = input()


a = sorted(a)
b = sorted(b)


def are_same(i):
    if a[i] == b[i] :
        return True
    else:
        return False


if len(a) != len(b):
    print("No")
else:
    for j in range(len(a)):
        if are_same(j):
            if j == len(a)-1:
                print("Yes")
        else:
            print("No")
            break