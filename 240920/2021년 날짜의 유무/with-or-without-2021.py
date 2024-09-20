m, d = tuple(map(int, input().split()))

def check_date(m, d):
    if m > 12 or d > 31:
        return False
    else:
        if m % 2 == 0:
            if m == 2:
                if d > 28:
                    return "No"
                else:
                    return "Yes"
            elif m == 8:
                if  d > 31:
                   return "No"
                else:
                    return "Yes"
            else: 
                if d > 30:
                    return "No"
                else:
                    return "Yes"

        else:
            if d > 31:
                return "No"
            else:
                return "Yes"


print(check_date(m,d))