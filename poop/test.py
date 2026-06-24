class Student:
    college = "ABC"

    def __init__(self, name):
        self.name = name

s1 = Student("Raghav")
s2 = Student("Aman")

s1.college = "XYZ"

print(s1.college)
print(s2.college)
print(Student.college)