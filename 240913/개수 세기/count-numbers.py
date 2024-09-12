init = input()
n = init.split()[0]
m = init.split()[1]

arr = list(map(int, input().split()))

print(arr.count(int(m)))