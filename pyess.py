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
























