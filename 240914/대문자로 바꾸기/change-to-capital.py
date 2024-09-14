di = ord('a') - ord('A')

for i in range(5):
    arr = list(map(str, input().split()))
    for j in range(3):
        print(chr(ord(arr[j])-di), end=" ")
    print()