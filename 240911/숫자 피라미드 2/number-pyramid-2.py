n = int(input())

cnt = 1
for i in range(n):
    for j in range(n):
        if i < j:
            continue
        else:     
            print(f"{cnt}", end=" ")
            cnt += 1
    print()


#(0,0)
#(1,0) (1,1)
#(2,0) (2,1) (2,2)
#()