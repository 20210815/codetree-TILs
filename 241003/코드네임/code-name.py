class Student:
    def __init__ (self, codename="", score=0):
        self.codename = codename
        self.score = score

student_list = [Student() for _ in range(5)]

for i in range(5):
    codename, score = tuple(map(str, input().split()))
    student_list[i] = Student(codename, int(score))


def check_score(n = 5):
    mini = 100
    num = 0
    for i in range(n):
        if student_list[i].score < mini:
            mini = student_list[i].score
            num = i
    return num


index = check_score()
print(f'{student_list[index].codename} {student_list[index].score}')