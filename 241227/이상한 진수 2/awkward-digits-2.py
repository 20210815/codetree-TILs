a = list(input())

count = 0

if len(a) == 1:
    if a[0] == '1':
        a[0] = 0
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