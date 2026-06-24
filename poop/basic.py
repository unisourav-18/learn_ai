class  Student:
    College_Name = "ABC College"

    def __init__(self, name, std):
        self.name = name
        self.std = std

    def welcome(self):
        print("welcome student: ", self.name)

    def get_std(self):
        print("studies in:", end=' ')
        return self.std

s1 = Student("Raghav", "12th")
s1.welcome()
print(s1.name)
print(s1.std)
print(s1.get_std())
