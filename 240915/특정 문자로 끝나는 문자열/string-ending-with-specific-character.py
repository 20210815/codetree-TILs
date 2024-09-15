string = []

while True:
    s = input()
    string.append(s)
    if len(s) == 1:
        break

for i in range(len(string)-1):
    if s == string[i][len(string[i])-1]:
        print(string[i])