class Meet:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time


code, point, time = tuple(map(str, input().split()))
meet1 = Meet(code, point, time)
print(f"secret code : {meet1.code}")
print(f"meeting point : {meet1.point}")
print(f"time : {meet1.time}")