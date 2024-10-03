class User:
    def __init__ (self, id, lvl):
        self.id = id
        self.lvl = lvl


user1 = User("codetree", 10)

arr = tuple(map(str, input().split()))

user2 = User(arr[0], arr[1])

print(f'user {user1.id} lv {user1.lvl}')
print(f'user {user2.id} lv {user2.lvl}')