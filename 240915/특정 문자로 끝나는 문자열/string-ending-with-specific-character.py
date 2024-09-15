string = [''] * 10

for i in range(10):
    string[i] = input()

s = input()

cnt = 0
for i in range(len(string)):
    if s == string[i][len(string[i])-1]:
        cnt += 1 
        print(string[i])
    elif cnt == 0 and i == len(string)-1:
        print("None")