class Ur:
    def __init__(self, name="", addr="", city=""):
        self.name= name
        self.addr = addr
        self.city = city

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
people = [Ur(name, addr, city) for name, addr, city in arr]

target_idx = 0
for i, person in enumerate(people):
    if person.name > people[target_idx].name:
        target_idx = i


print(f'name {people[target_idx].name}')
print(f'addr {people[target_idx].addr}')
print(f'city {people[target_idx].city}')