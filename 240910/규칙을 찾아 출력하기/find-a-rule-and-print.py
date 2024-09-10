n = int(input())

# (1,1), (1,2)
#        (2,2)

# (1,1) (1,2) (1,3)
#       (2,2) (2,3)
#             (3,3)


for i in range(n):
    for j in range(n):
        if (i == 0) or (i == n-1) or (j == n-1):
            print("*", end= " ")
            
        elif i >= 1:
            if (i == j) or (j > i):
                print(" ", end= " ")
            else:
                print("*", end = " ")
    print()