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

# def compute_monthly_payment(loan_amount, years, annual_interest_rate):
#     monthly_interest_rate = annual_interest_rate / 12 / 100
#     months = years * 12
#     monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -months)
#     return monthly_payment

# # Input values from the user
# loan_amount = float(input("Enter the loan amount: $"))
# years = int(input("Enter the number of years: "))
# annual_interest_rate = float(input("Enter the annual interest rate (in percentage): "))

# # Compute the monthly payment
# monthly_payment = compute_monthly_payment(loan_amount, years, annual_interest_rate)

# # Display the result
# print("The monthly payment is: $", round(monthly_payment, 2))

# f = open("mango.txt", "r")
# f.read()
# data = f.tell()
# print(data)

# oldfile = open("mango.txt","r")
# data = oldfile.read()

# newfile = open("lichi.txt","w")
# newfile.write(data)

# import json

# data = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }

# serialized_data = json.dumps(data)

# print(type(serialized_data))


# # Sample serialized JSON data
# serialized_data = '{"name": "John", "age": 30, "city": "New York"}'

# # Deserialize the JSON data to Python dictionary
# deserialized_data = json.loads(serialized_data)

# # Print the deserialized data
# print(type(deserialized_data))

# 1. Open the file if exists, if not create a new file
# file = open("test.txt", "a+")
# print("File 'test.txt' opened successfully.")

# file = open("test.txt", "w+")
# print("File 'test.txt' created successfully.")

# # # 2. Add string 'abcde' to the end of the file
# file.write("abcde")
# print("String 'abcde' added to the end of the file.")

# # # 3. Read and display first 5 characters
# file.seek(0)  # Move the file pointer to the beginning of the file
# first_five_chars = file.read(5)
# print("First 5 characters:", first_five_chars)

# # # 4. Display total number of characters present in the file
# file.seek(0)  # Move the file pointer to the beginning of the file
# total_characters = len(file.read())
# print("Total number of characters in the file:", total_characters)
# file.close()






