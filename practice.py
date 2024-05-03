# string methods in python

# 1.concat
# a = "hello"
# b = " world"
# print(a+b)

# 2.Length of str
# a = "onkar"
# print(len(a))

# 3.Indexing
# a = "onkar"
# print(a[0])
# print(a[5])
# print(a[2])

# 4.slicing
# a = "onkar"
# print(a[1:3])
# print(a[2:])
# print(a[:2])
# print(a[-3:-1])

# String functions
# 1.endswith()
# a = "onkar"
# print(a.endswith("m"))
# 2.capitalize()
# print(a.capitalize())
# print(a.replace("onkar","GM"))
# print(a.find("t"))
# b = "apple"
# print(b.count("p"))

# practice q)
# a = input("fname: ")
# print(len(a))

# nesting if:
# amount = int(input("Amount: "))
# if amount%100==0:
#     if amount>=500:
#         notes = amount//500
#         print("500 notes are ",notes)
#         amount = amount%500
#     if amount >= 200:
#         notes = amount//200
#         print("200 notes are ",notes)
#         amount = amount%200
#     if amount>=100:
#         notes = amount//100
#         print("100 notes are ",notes)
# else:
#     print('Please put value in multiple of 100')

# list & tuples:
# a = "onkar"
# print(a[0])
# a[0]="m"

# list slice
# a= [1,2,3,4,5]
# print(a[1:3])
# print(a[-3:-2])

# list methods
# 1.append
# a = [1,2,3,4,5]
# a.append(6)
# print(a)

# 2.sort
# a = [2,3,1,5]
# a.sort(reverse=True)
# print(a)

# 3.reverse
# a=["onkar","max","raj"]
# a.reverse()
# print(a)

# 4.index
# a = [1,2,3,4]
# a.insert(2,"on")
# print(a)

# 5.remove and 6.pop
# a = [1,2,3,4,5]
# a.remove(4)
# a.pop(1)
# print(a)

# tuples:
# a = (1,2,3,4,5)
# print(a[0])
# a[0]=2
# print(a)

# methods
# 1.index
# print(a.index())
# 2.count
# a = [1,1,2,3,5,]
# print(a.count(1))

# check if list is palindrome no 
# a = [1,2,3,2,1]
# # a = [1,2,3]
# b = a.copy()
# # print(b)
# b.reverse()
# if b==a:
#     print("It is palindrome list")
# else:
#     print("not p")

# Dictionary
# a = {"name":"onkar", "age":24}
# # print(type(a))
# # print(a["name"])
# a["name"]="raj"
# print(a)

# nested dictionary
# a = {
#     "name":"onkar",
#     "age:": 24,
#     "courses":{"FSD":"python", "DSA": "JS"}
# }
# dict methods

# print(a.keys())
# print(a.values())
# print(a.items())
# print(a.get('name'))
# a.update({"city":"thane"})
# a.update({'courses':{'c':'code'}})
# print(a)

# set:
# a = {1,2,3,6,"onkar"}
# a.add(5)
# a.remove(5)
# a.clear()
# a.pop()
# a = {1,2,3}
# b = {5,6,7}
# print(a.union(b))
# a = {1,2,3}
# b = {1,5,6}
# print(a.intersection(b))





