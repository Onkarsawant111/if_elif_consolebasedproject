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

# class Students:
#     @staticmethod
#     def greet():
#         print("hello")

# s1 = Students
# s1.greet()      

# 1.abstraction
# class Car:
#     def __init__(self):
#         self.engine = False
#         self.gear = False
#     def start(self):
#         self.engine = True
#         self.gear = True
#         print("car started")

# car1 = Car()
# car1.start()

# 2.encapsulation

# class Bank_account:
#     def __init__(self, account_no, balance ):
#         self.account_no = account_no
#         self.balance = balance

#     def credit(self, amount):
#         self.balance = self.balance + amount
#         print("total balance =", self.bal())
    
#     def debit(self, amount):
#         self.balance = self.balance - amount
#         print("total balance =", self.bal())
    
#     def bal(self):
#         final_amount = self.balance
#         return final_amount
    
# acc1 = Bank_account(123,10000)
# acc1.debit(500)

# private attributes
# class Students:
#     def __init__(self, name):
#         self.__name = name

# s1 = Students("onkar")
# print(s1.__name)

# 3. Inheritance

# class Car:
#     @staticmethod
#     def start():
#         print("car started")
    
# class Toyota(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = Toyota("fortuner")
# car1.start()

#multiple inheritance:
# class keyplugin:
#     def start(self):
#         print("car started")
    
# class keyplugoff:
#     def stop(self):
#         print("car stopped")

# class engine(keyplugin,keyplugoff):
#     def go(self):
#         print("lets go")

# car1 = engine()
# car1.start()
# car1.stop()

# super keyword

# class Car:
#     def __init__(self, type):
#         self.type = type
    
# class Toyota(Car):
#     def __init__(self, name, type):
#         self.name = name
#         super().__init__(type)   

# car1 = Toyota("fortuner", "electric")
# print(car1.type)

# class method

# class Person:
#     name = "anonymous"
#     def changename(self,name):
#         self.name = name
# p1 = Person()
# p1.changename("onkar")
# print(Person.name)

# class Person:
#     name = "anonymous"
#     @classmethod
#     def changename(cls,name):
#         cls.name = name
# p1 = Person()
# p1.changename("onkar")
# print(Person.name) 

# property method
# class Marks:
#     def __init__(self, phy , chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
        
#     @property
#     def cal(self):
#         return (self.phy + self.chem + self.math)/3
# s1 = Marks(98,96,95)
# s1.phy = 85
# print(s1.cal)

# 4. Polymorphism
# print([1,2,3] + [4,5,6])

# 1.operator overloading
# class Complex:  
#         def __init__(self,real,img):
#                 self.real = real
#                 self.img = img
        
#         def showno(self):
#                 print(self.real,"i","+",self.img,"j")
        
#         def __add__(num1,num2):
#                 newreal = num1.real + num2.real
#                 newimg = num1.img + num2.img
#                 return Complex(newreal, newimg)

# num1 = Complex(4,5)
# num2 = Complex(1,3)
# result = num1 + num2




























