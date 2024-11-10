m1, d1, m2, d2 = tuple(map(int, input().split()))

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def calculateDate(m, d):
    result = 0
    for i in range(m):
        result += num_of_days[i]
    result += d
    return result


date1 = calculateDate(m1, d1)
date2 = calculateDate(m2, d2)

match (date2-date1) % 7:
    case 0: print("Mon")
    case 1: print("Tue")
    case 2: print("Wed")
    case 3: print("Thu")
    case 4: print("Fri")
    case 5: print("Sat")
    case 6: print("Sun")