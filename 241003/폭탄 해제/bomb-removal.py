class Code:
    def __init__(self, hcode, color, time):
        self.hcode = hcode
        self.color = color
        self.time = time

hcode, color, time = tuple(map(str, input().split()))
code1 = Code(hcode, color, time)

print(f'code : {code1.hcode}')
print(f'color : {code1.color}')
print(f'second : {code1.time}')