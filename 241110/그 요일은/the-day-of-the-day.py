m1, d1, m2, d2 = tuple(map(int, input().split()))
day = input()

week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def calculateDate(m, d):
    result = 0
    for i in range(m):
        result += num_of_days[i]
    result += d
    return result


date1 = calculateDate(m1, d1)
date2 = calculateDate(m2, d2)
term = date2-date1

if term % 7 >= week.index(day):
    print(term // 7 + 1)
elif day == "Mon":
    print(term // 7 + 1)
else:
    print(term // 7)