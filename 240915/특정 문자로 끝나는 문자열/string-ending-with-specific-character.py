string = []

while True:
    s = input()
    string.append(s)
    if len(s) == 1:
        break

cnt = 0
for i in range(len(string)-1):
    if s == string[i][len(string[i])-1]:
        cnt += 1 
        print(string[i])
    elif cnt == 0 and i == len(string)-1:
        print("None")