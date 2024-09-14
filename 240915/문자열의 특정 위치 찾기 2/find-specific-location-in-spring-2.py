arr= ['apple', 'banana', 'grape', 'blueberry', 'orange']

ch = input()

cnt = 0
for i in range(5):
    if arr[i][3-1] == ch or arr[i][4-1] == ch:
        cnt += 1
        print(arr[i])
print(cnt)