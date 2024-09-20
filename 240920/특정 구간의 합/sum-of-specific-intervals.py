n, m = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

def get_sum(a1, a2):
    sum = 0
    for i in range(a1-1, a2):
        sum += arr[i]
    return sum

for i in range(m):
    a1, a2 = tuple(map(int, input().split()))
    print(get_sum(a1, a2))