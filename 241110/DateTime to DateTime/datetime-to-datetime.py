day, hour, minute = tuple(map(int, input().split()))


def calculateTime(d, h, m):
    result = 0
    result += m
    result += h * 60
    result += d *24 * 60
    return result


if day == 11:
    if hour < 11:
        print(-1)
    elif hour == 11:
        if minute < 11:
            print(-1)
        else:
            time1 = calculateTime(11, 11, 11)
            time2 = calculateTime(day, hour, minute)
            print(time2-time1)
else:
    time1 = calculateTime(11, 11, 11)
    time2 = calculateTime(day, hour, minute)
    print(time2-time1)