a1 = input()

anum = list(map(int, a1.split()))

print(sum(anum))
print("%d" %(round(sum(anum)/len(anum))))