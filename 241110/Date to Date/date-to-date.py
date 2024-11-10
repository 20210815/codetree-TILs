num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m1, d1, m2, d2 = tuple(map(int, input().split()))


day1 = 0
day2 = 0
for i in range(m1):
    day1 += num_of_days[i]

day1 += d1

for i in range(m2):
    day2 += num_of_days[i]

day2 += d2

print(day2-day1+1)