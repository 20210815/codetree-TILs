a = input()
a = a.split()
a[0] = int(a[0])
a[1] = int(a[1])

print(sum(a), sum(a)/len(a))