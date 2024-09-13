arr_ind = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))
# 1 5 2 6
# 5 6


# 4 1 3 1 3 1 4


# 9 2 4 1 3 3 1 4 6 8
# 4 1 3 1 3 1 4

for i in range(len(b)):
    if b[i] not in a:
        print("No")
    for j in range(len(a)):
        if b[i] == a[j]:
            i += 1
        else:
            break
    if j != len(b):
        print("No")
        break
if i == len(b):
    print("Yes")