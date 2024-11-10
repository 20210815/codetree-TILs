m1, d1, m2, d2 = tuple(map(int, input().split()))
day = input()


num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def calculateDate(m, d):
    result = 0
    for i in range(m):
        result += num_of_days[i]
    result += d
    return result


date1 = calculateDate(m1, d1)
date2 = calculateDate(m2, d2)

print((date2-date1)//7+1)