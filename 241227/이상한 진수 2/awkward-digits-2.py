a = list(input())

count = 0

#만약 1만 있다면
if set(a) == {'1'}:
    for index in range(len(a)-1, -1, -1):
        if int(a[index]) == 1:
            a[index] = '0'
            count += 1
        if count == 1:
            break
else:
    for index in range(len(a)):
        if int(a[index]) == 0 :
            a[index] = '1'
            count += 1
        if count == 1:
            break

result = 0
for index in range(len(a)):
    if int(a[index]) == 1:
        result += 2 ** (len(a)-index-1)

print(result)