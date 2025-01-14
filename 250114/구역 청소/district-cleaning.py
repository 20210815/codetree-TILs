a, b = map(int, input().split())
c, d = map(int, input().split())

# Write your code here!
def intersecting(a, b, c, d):
    if b < c or d < a:
        return False
    else:
        return True


clean = 0
if not intersecting(a,b,c,d):
    clean = (b-a) + (d-c)
else:
    #겹치는 부분
    clean = max(a,b,c,d) - min(a,b,c,d)

print(clean)