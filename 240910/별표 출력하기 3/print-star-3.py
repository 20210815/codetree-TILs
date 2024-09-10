n = int(input())

for i in range(n):
    for k in range(i): # 0 
        print(" ", end=" ")
    for j in range( 2 * (n-i) - 1):         # 5
        print("*", end=" ")
    print()