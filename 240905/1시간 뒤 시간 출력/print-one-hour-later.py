time = input()

time = time.split(":")

print("%d:%d" %(int(time[0])+1, int(time[1])))