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

# class Students:
#     collegename = "abc"
#     def __init__(self, fullname):
#         self.name = fullname
#         print("new student added =", fullname)

# s1 = Students("onkar")
# s2 = Students("raj")
# print(s1.name)
# print(s2.collegename)

# class Students:
#     schoolname = "snvm"
#     def __init__(self , name):
#         self.name = name
#     def greet(self):
#         print("hello", self.name)

# s1 = Students("onkar")
# s1.greet()

# class Student:
#     def __init__(self,name,m1,m2,m3):
#         self.name = name
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
    
#     def avg(self):
#         return (self.m1+self.m2+self.m3)/3
    
# s1 = Student("onkar",92,89,94)
# print(s1.avg())

class Students:
    @staticmethod
    def greet():
        print("hello")

s1 = Students
s1.greet()      


















