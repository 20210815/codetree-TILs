n = list(map(str, input().split()))
string = n[0]
q = int(n[1])

for i in range(q):
    sh = int(input())
    if sh == 1:
        string = string[1:] + string[0]
    elif sh == 2:
        string = string[-1] + string[:-1]
    else:
        string = string[::-1]
    print(string)