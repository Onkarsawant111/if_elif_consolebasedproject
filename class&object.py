# class Student:
#     name = "onkar"

# s1 = Student()
# print(s1.name)

# class Cars:
#     color = "blue"
# bmw = Cars()
# print(bmw.color)

# class Cars:
#     def __init__(self):
#         print("new car with blue color")
#     color = "blue"

# bmw = Cars()
# print(bmw)

class Students:
    collegename = "abc"
    def __init__(self, fullname):
        self.name = fullname
        print("new student added =", fullname)

s1 = Students("onkar")
s2 = Students("raj")
print(s1.name)
print(s2.collegename)























