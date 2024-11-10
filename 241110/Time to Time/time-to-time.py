T1, M1, T2, M2 = tuple(map(int, input().split()))

total1 = 0
total2 = 0

if T1 != 0:
    total1 = T1 * 60 + M1
if T2 != 0:
    total2 = T2 * 60 + M2


print(total2-total1)