n = int(input())

string = []

for i in range(n):
    string += input()

for i in range(len(string)):
    print(string[i], end="")