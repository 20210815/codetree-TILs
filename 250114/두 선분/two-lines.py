x1, x2, x3, x4 = map(int, input().split())

# Write your code here!
def intersecting(x1, x2, x3, x4):
    if x2 < x3 or x4 < x1:
        return False
    else:
        return True

if intersecting(x1, x2, x3, x4):
    print('intersecting')
else:
    print('nonintersecting')