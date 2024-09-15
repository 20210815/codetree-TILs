a = input()
b = input()



for i in range(len(list(a))):
    if b in a:
        ind = a.index(b)
        a = a[0:ind] + a[ind+len(list(b)):]
    else:
        break
print(a)