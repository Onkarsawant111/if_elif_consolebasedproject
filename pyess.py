# print(type((int(input("age: ")))))

# vinitial = float(input("initial velocity = "))
# vfinal = float(input("final velocity = "))
# time = int(input("time taken by car to travel a distance = "))
# acc = (vfinal - vinitial)/time
# print("accelartion of car is",acc,"m/s")

# i = 100
# sum = 0
# while i <= 200:
#     if i % 2 == 0:
#         sum = sum + i
#     i = i + 1
# print(sum)

# p = float(input("principle = "))
# n = float(input("no of years = "))
# r = float(input("rate of interest = "))
# sinterest = (p*n*r)/100
# print(sinterest,"rs")

# r = 1 
# while r <= 5:
#     c = 1
#     while c <= 5:
#         if c <= r:
#             print(r, end=" ")
#         c = c + 1
#     print()
#     r = r + 1

# a =[10,20,[15,25,35],40]
# print(a[2][2])

# def remove(s):
#     vow = "aeiouAEIOU"
#     r = " "
#     for i in s:
#         if i not in vow:
#             r = r + i
#     return r 

# ip = input("enter string: ")
# print(remove(ip))

# import random
# random_integers = [random.randint(1, 10) for i in range(10)]

# odd_list = []
# even_list = []

# for num in random_integers:
#     if num % 2 == 0:
#         even_list.append(num)
#     else:
#         odd_list.append(num)

# print("Original list:", random_integers)
# print("Odd numbers:", odd_list)
# print("Even numbers:", even_list)

# Define an empty dictionary to store friends' names and phone numbers
# friends_dict = {}

# Function to print the dictionary in sorted order
# def print_sorted_dict():
#     sorted_keys = sorted(friends_dict.keys())
#     for key in sorted_keys:
#         print(f"{key}: {friends_dict[key]}")

# # Prompt the user to enter the name and check if it's present in the dictionary
# name = input("Enter a friend's name: ")
# if name in friends_dict:
#     print(f"The phone number of {name} is {friends_dict[name]}.")
# else:
#     phone_number = input(f"{name} is not in the dictionary. Enter their phone number: ")
#     friends_dict[name] = phone_number
#     print("Details added successfully.")

# # Print the dictionary in sorted order
# print("\nFriends' list (sorted by name):")
# print_sorted_dict()

# arguments/parameters in function :

# def show(val=2):
#     return val * 2
# print(show())

# def user(name,age):
#     print(f"username is {name} and age is {age}")
# user(24,"onkar")

# def user(name,age):
#     print(f"username is {name} and age is {age}")
# user(age= 24, name="onkar")

# def user(*args):
#     print(args)
# user(1,2,3)

# def user(**kwargs):
#     print(type(kwargs))
# user(name="onkar",city="thane")

# square = lambda x: x ** 2
# print(square(5))  

# s=lambda x,y : x if x>y else y

# num1=int(input("Enter first number"))

# num2=int(input("Enter second number"))

# print("largest number : ",s(num1,num2))

# def square(x):
#     return x ** 2

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(square, numbers)
# print(list(squared_numbers))

# from functools import reduce

# def subtract(x, y):
#     print(x)
#     print(y)
#     return x - y

# numbers = [1, 2, 3, 4, 5]

# # Without initializer
# result_without_initializer = reduce(subtract, numbers)
# print("Without initializer:", result_without_initializer)  # Output: -13

# # With initializer
# initializer = 100
# result_with_initializer = reduce(subtract, numbers, initializer)
# print("With initializer:", result_with_initializer)  # Output: 85

# from my_package import demo
# a = demo.add(5,5)
# print(a)









