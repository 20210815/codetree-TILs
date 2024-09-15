string = input()

inst = input()

for i in range(len(inst)):
    if inst[i] == 'L':
        string = string[1:] + string[0]
    elif inst[i] == 'R':
        string = string[-1] + string[:-1]

print(string)