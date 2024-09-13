arr = list(map(int, input().split()))

# 500 미만
# 500 초과 중 가장 작은
more = []
less = []

for i in arr:
    if i < 500:
        less.append(i)
    elif i > 500:
        more.append(i)

more.sort()
less.sort()

print(less[len(less)-1], more[0])