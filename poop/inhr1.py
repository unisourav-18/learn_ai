# class Person:
#     __name = "anonymous"

#     def __hello(self):
#         print("hello person!")

#     def welcome(self):
#         self.__hello()

# p1 = Person()

# print(p1.welcome())

class Person:
    __name = "anonymous"

    def get_name(self):
        return self.__name

p1 = Person()

print(p1.get_name())
print(Person._Person__name)