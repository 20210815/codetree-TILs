n = int(input())
arr = list(map(float, input().split()))


avg = sum(arr)/len(arr)

print("%.1f" %avg)
if avg >= 4.0:
    print("Perfect")
elif avg >= 3.0:
    print("Good")
else:
    print("Poor")