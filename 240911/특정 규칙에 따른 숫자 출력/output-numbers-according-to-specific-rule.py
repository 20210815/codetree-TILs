n = int(input())

cnt = 1
for i in range(n):
    for j in range(n):
        if i <= j:
            print(f"{cnt}", end=" ")
            cnt += 1
            if cnt > 9:
                cnt = 1
        else:
            print(" ", end=" ")
    print()


#(0,0) (0,1)
#       (1,1)