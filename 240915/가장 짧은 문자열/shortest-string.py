n = len(input())
m = len(input())
o = len(input())

max = n
min = n

if max < m:
    max = m
    if min > o:
        min = o
if max < o:
    max = o
    if min > m:
        min = m

print(max - min)