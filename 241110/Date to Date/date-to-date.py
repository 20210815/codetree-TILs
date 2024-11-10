num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m1, d1, m2, d2 = tuple(map(int, input().split()))


result = 0
for i in range(m1-1, m2):
    if m1-1 == i:
        result += num_of_days[i] - d1
    elif m2-1 == i:
        result += d2
    else:
        result += num_of_days[i]


print(result)