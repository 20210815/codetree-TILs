inpu = list(map(str, input().split()))

print(ord(inpu[0]) + ord(inpu[1]), end=" ")
if ord(inpu[0]) > ord(inpu[1]):
    print(ord(inpu[0]) - ord(inpu[1]), end=" ")
else:
    print(ord(inpu[1]) - ord(inpu[0]), end=" ")