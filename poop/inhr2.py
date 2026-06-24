class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")

class ToyotaCar(Car): # Class Inherited
    def __init__(self, name):
        self.name = name

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()
print(car1.type)

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")

print(car1.color)
print(car1.name)
print(car2.name)