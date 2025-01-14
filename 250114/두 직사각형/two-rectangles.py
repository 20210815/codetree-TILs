x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# Write your code here!
def overlapping(x1, y1, a1, b1, x2, y2, a2, b2):
    if x2 < a1 or y2 < b1 or a2 < x1 or b2 < y1:
        return False
    else:
        return True

if overlapping(x1, y1, a1, b1, x2, y2, a2, b2):
    print("overlapping")
else:
    print("nonoverlapping")
