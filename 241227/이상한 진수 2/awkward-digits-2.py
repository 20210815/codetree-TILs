a = list(input())

count = 0
for index in range(len(a)):
    if int(a[index]) == 0 :
        a[index] = '1'
        count += 1
    if count == 1:
        break

result = 2
for index in range(len(a)):
    if int(a[index]) == 1:
        for j in range(len(a)-index-1):
            result*=2

print(result)