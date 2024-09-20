def date_exists(y, m, d):
    if m > 12 or d > 31:
        return -1
    else:
        if m == 2:
            if four_years(y):
                if d > 29:
                    return -1
            else:
                if d > 28:
                    return -1
        elif m == 8:
            if d > 31:
                return -1
        elif m % 2 == 0:
            if d > 30:
                return -1
        else:
            if d > 31:
                return -1
        return weather(m)

def weather(m):
    if m >= 3 and m <= 5:
        return "Spring"
    elif m >= 6 and m <= 8:
        return "Summer"
    elif m >= 9 and m <= 11:
        return "Fall"
    else:
        return "Winter"
    

def four_years(y):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 == 0:
            return True
        elif y % 100 != 0:
            return True
        else:
            return False
    else:
        return False


y, m ,d = list(map(int, input().split()))
print(date_exists(y, m, d))