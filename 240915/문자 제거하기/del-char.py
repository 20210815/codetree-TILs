n = list(input())

while True:
    if len(n) == 1:
        break
    index = int(input())
    if index >= len(n):
        n.pop()
    else:
        n.pop(index)
    
    for i in range(len(n)):
        print(n[i], end="")
    print()