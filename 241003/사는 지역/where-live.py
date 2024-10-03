class Ur:
    def __init__(self, name="", addr="", city=""):
        self.name= name
        self.addr = addr
        self.city = city

n = int(input())
name_list = [''] * n
user = [Ur() for _ in range(n)]

for i in range(n):
    name, addr, city = tuple(map(str, input().split()))
    user[i] = Ur(name, addr, city)
    name_list[i] = name

name_list.sort(reverse=True)

for i in range(n):
    if user[i].name == name_list[0]:
        print(f'name {user[i].name}')
        print(f'addr {user[i].addr}')
        print(f'city {user[i].city}')