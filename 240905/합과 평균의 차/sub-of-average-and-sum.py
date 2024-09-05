ini = input()

li = list(map(int, ini.split()))

print(sum(li))
print(sum(li)//(len(li)))
print(sum(li)- (sum(li)//len(li)))