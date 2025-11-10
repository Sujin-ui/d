class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

# 객체 생성
s1 = Student("주A", 101)
s1.add_grade(90)
s1.add_grade(85)

print(f"{s1.name}의 평균 점수: {s1.get_average()}")