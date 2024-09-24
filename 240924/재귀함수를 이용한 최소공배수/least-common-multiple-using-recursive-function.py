n = int(input())
arr = list(map(int, input().split()))


# 1 2 3 4 5 6 7 8 9 10
#       2   3   4    5

def get_lmd(n):
    if n == 0:
        return arr[0]
    return arr[n] * get_lmd(n-1)


def get_gcd(n):
    gcd = 1
    for i in range(n): #n번 돌면서...
        for k in range(1,arr[i]+1):
            if arr[i] % k != 0:
                break
        gcd = i
        arr[i] = gcd

get_gcd(n)
print(get_lmd(n))

#1 2 3 5 7 3