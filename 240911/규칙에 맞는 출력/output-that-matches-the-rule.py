n = int(input())

for i in range(n, 0, -1):
    for j in range(n-i+1):
        print(f"{i+j}", end=" ")
    print()


#(5,5)
#(4,5) (4,4)
#(2,0) (2,1) (2,2)
#(3,0) (3,1)
#  4,0 4,1 
#1 2 3 4