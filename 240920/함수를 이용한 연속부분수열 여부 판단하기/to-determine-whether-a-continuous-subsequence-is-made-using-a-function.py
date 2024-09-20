a, b = tuple(map(int, input().split()))

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

def check_list(a_list, b_list, a, b):
    if a < b:
        return "No"
    for i in range(b):
        for j in range(a):
            if b_list[i] == a_list[j]:
                while True:
                    if i > b or j > a:
                        return "No"
                    if b_list[i] == a_list[j]:
                        i += 1
                        j += 1
                        if i == b:
                            return "Yes"
                    else:
                        return "No"
                    


print(check_list(a_list, b_list, a, b))