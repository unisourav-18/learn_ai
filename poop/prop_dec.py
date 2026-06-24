#simple basic use case of property decorator

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percent(self):
        return str((self.phy + self.chem + self.math)/3) + "%"

s1 = Student(98,99,97)
print(s1.percent)
s1.phy = 95
print(s1.percent)